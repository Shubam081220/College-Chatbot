import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.chatbot import get_response

st.title("🎓 College Chatbot")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("You:", key="user_input")

if user_input:
    response = get_response(user_input)
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", response))

for speaker, message in st.session_state.history:
    st.markdown(f"**{speaker}:** {message}")

from fpdf import FPDF
import tempfile

def export_chat_as_pdf(chat_history):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for speaker, message in chat_history:
        pdf.multi_cell(0, 10, f"{speaker}: {message}\n")

    # Save to temporary file
    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdf.output(temp.name)
    return temp.name

if st.button("📄 Download Chat History as PDF"):
    if st.session_state.history:
        pdf_path = export_chat_as_pdf(st.session_state.history)
        with open(pdf_path, "rb") as f:
            st.download_button("Click to Download", f, file_name="chat_history.pdf")
