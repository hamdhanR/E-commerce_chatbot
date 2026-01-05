# 🛒 Ecommerce Chatbot

A Streamlit-based chatbot that answers user questions about product prices, availability, and comparisons across multiple e-commerce platforms (like Amazon, Flipkart, Temu) using MongoDB and LLM-powered queries.

---

## Features

- Ask about cheapest or highest-rated products.
- Compare prices across platforms.
- Find products under a specific price.
- Check availability across platforms.
- Provides clear, user-friendly answers with platform URLs.

---

## Project Structure

app/
│
├── main.py     # Streamlit frontend
├── models.py   # MongoDB table schema and description
├── chatbot.py  # Core chatbot logic using LLMs
├── database.py # MongoDB connection
├── llm.py      # Gemini LLM initialization
└── utils.py    # Helper functions

Create a virtual environment and activate it:
python -m venv venv
venv\Scripts\activate      # Windows

Install dependencies:
pip install -r requirements.txt

Create a .env file in the project root with your Gemini API key:
GEMINI_API_KEY=your_api_key_here

Ensure MongoDB is running locally (mongodb://localhost:27017) and contains your collections (e.g., smartphones).

## MongoDB Setup

Database: e-commerce

Collection: smartphones

Schema:

platform: string
category: string
product_id: string
product_name: string
brand: string
price: float
currency: string
rating: float
reviews_count: integer
specs: object
availability: string
platform_url: string

# Run the app
streamlit run app/main.py

### Example Usage

1.Cheapest iPhone 15 on Amazon and Flipkart

2.List all smartphones under 2000 AED

3.Compare prices of Samsung Galaxy S23 across platforms