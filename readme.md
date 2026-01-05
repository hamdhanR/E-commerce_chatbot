# 🛒 Ecommerce Chatbot

A Streamlit-based chatbot that answers user questions about product prices, availability, and comparisons across multiple e-commerce platforms (like Amazon, Flipkart, Temu) using MongoDB and LLM-powered queries.

---

## Features

- Ask about cheapest or highest-rated products.
- Compare prices across platforms.
- Find products under a specific price.
- Check availability across platforms.
- Provides clear, user-friendly answers.

---

## Project Structure

<img width="586" height="245" alt="image" src="https://github.com/user-attachments/assets/d213924d-11fe-4cb7-bf42-8b98747f7631" />


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


## Output images
<img width="1509" height="954" alt="Screenshot 2026-01-05 134109" src="https://github.com/user-attachments/assets/047d06f5-442e-4e31-ba28-f144829368ef" />
<img width="1589" height="960" alt="Screenshot 2026-01-05 134130" src="https://github.com/user-attachments/assets/178766e5-f7a0-428d-a07f-c6ac170708c0" />
<img width="1507" height="959" alt="Screenshot 2026-01-05 134148" src="https://github.com/user-attachments/assets/d16ce218-e2d7-4d56-b98d-db1bf2564da9" />





