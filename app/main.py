# app/main.py
import streamlit as st
from chatbot import answer_user_question

# ----------------------------
# Streamlit Page Config
# ----------------------------
st.set_page_config(
    page_title="Ecommerce Chatbot",
    page_icon="🛒",
    layout="centered"
)

st.title("🛒 Ecommerce Chatbot")
st.write("Ask questions about products and prices across platforms!")

# ----------------------------
# Session state for chat history
# ----------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# ----------------------------
# User input
# ----------------------------
user_question = st.text_area(
    "Enter your question here:",
    height=80
)

if st.button("Submit"):
    if user_question.strip():
        # Call your chatbot function
        answer = answer_user_question(user_question)

        # Save to session state
        st.session_state.history.append({"question": user_question, "answer": answer})

        # Clear text area
        user_question = ""

# ----------------------------
# Display chat history
# ----------------------------
if st.session_state.history:
    st.write("### Chat History")
    for i, chat in enumerate(st.session_state.history, 1):
        st.markdown(f"**Q{i}:** {chat['question']}")
        st.markdown(f"**A{i}:** {chat['answer']}")
        st.write("---")
