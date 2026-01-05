# app/llm.py
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pathlib import Path

# Load .env from chatbot/
BASE_DIR = Path(__file__).resolve().parents[2]
load_dotenv(BASE_DIR / ".env")

llm_gemini = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.2,
    api_key=os.getenv("GEMINI_API_KEY"),
    max_tokens=800,
)
