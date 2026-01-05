# app/routes/chatbot.py
from langchain_classic.chains import LLMChain
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from llm import llm_gemini
from model import TABLE_SCHEMA, SCHEMA_DESCRIPTION
from database import db
from utils import extract_mongo_pipeline, safe_json_dumps

# ----------------------------
# LLM Prompt for MongoDB Query
# ----------------------------
system_msg = SystemMessagePromptTemplate.from_template(
    """
You are an expert in crafting MongoDB aggregation pipelines.
Use the table schema and schema description below to generate a pipeline for the user's question.

Rules:
- Return all matching products, unless asking for only cheapest or highest-rated.
- Match multiple platforms if mentioned.
- Match product_name exactly if possible, or using case-insensitive search.
- Support these query types:
  1. Cheapest product → return product(s) with lowest price.
  2. Highest-rated product → return product(s) with highest rating.
  3. Availability → return product(s) with their 'availability' field.
  4. Price comparison → return products from multiple platforms with the same name.
  5. Products under a specific price → return products where price <= specified value.
- Return ONLY the MongoDB pipeline as a JSON array, nothing else.

Example 1:
User question: "Find the cheapest iPhone 15 on Amazon and Flipkart."
MongoDB pipeline:
- Match documents where platform is "Amazon" or "Flipkart" and product_name is "iPhone 15"
- Sort the results by price in ascending order
- Limit the results to 1 document

Example 2:
User question: "List all smartphones under 2000 AED."
MongoDB pipeline:
- Match documents where category is "Smartphone" and price is less than or equal to 2000


Table schema:
{table_schema}

Schema description:
{schema_description}
"""
)

human_msg = HumanMessagePromptTemplate.from_template("{user_question}")
query_prompt = ChatPromptTemplate.from_messages([system_msg, human_msg])

llmchain = LLMChain(
    llm=llm_gemini,
    prompt=query_prompt,
    verbose=True
)

# ----------------------------
# LLM Prompt for Formatting Answer
# ----------------------------
formatter_system_msg = SystemMessagePromptTemplate.from_template(
    """
You are a helpful product comparison assistant.

Rules:
- Use ONLY the data provided.
- Explain results clearly and simply.
- Include platform URLs when possible.
- Compare platforms for price and rating if requested.
- If no products match the query, clearly say so.
- Respond in concise, readable text or bullet points for multiple results.

Example responses:
1. Cheapest product:
"The cheapest iPhone 15 is on Amazon for 3800 AED, rating 4.7. "
2. Highest-rated product:
"The highest-rated Samsung Galaxy S23 is on Flipkart with a rating of 4.9 and 12,450 reviews, priced at 69,999 INR"
3. Product availability:
"The iPhone 15 is currently in stock on Amazon and Temu, but out of stock on Flipkart."
4. Price comparison:
"Price comparison for iPhone 15:
- Amazon: 3800 AED
- Flipkart: 3899 AED
- Temu: 3750 AED
The cheapest is on Temu."
5. Products under a price:
"Smartphones under 1000 AED:
1. Xiaomi Redmi Note 12 is 950 AED , Rating: 4.5
2. Realme Narzo 60 is 890 AED , Rating: 4.3"

Return ONLY the final user-facing answer.
"""
)

formatter_human_msg = HumanMessagePromptTemplate.from_template(
    """
User question:
{user_question}

Product data (JSON):
{product_data}
"""
)

formatter_prompt = ChatPromptTemplate.from_messages(
    [formatter_system_msg, formatter_human_msg]
)

formatter_chain = LLMChain(
    llm=llm_gemini,
    prompt=formatter_prompt,
    verbose=True
)


# ----------------------------
# Chatbot Function
# ----------------------------
def answer_user_question(user_question: str, collection_name="smartphones"):
    collection = db[collection_name]

    # 1️⃣ Generate MongoDB query
    response_text = llmchain.run(
        user_question=user_question,
        table_schema=TABLE_SCHEMA,
        schema_description=SCHEMA_DESCRIPTION
    )

    pipeline = extract_mongo_pipeline(response_text)

    # 2️⃣ Execute MongoDB query
    results = list(collection.aggregate(pipeline))

    # 3️⃣ Format results for user
    if not results:
        return "I couldn't find any matching products for your query."

    return formatter_chain.run(
        user_question=user_question,
        product_data=safe_json_dumps(results)
    )
