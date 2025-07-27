# 🎓 College Chatbot

This is a smart college chatbot built using **Streamlit**, **Transformers (T5)**, and **Fuzzy FAQ Matching**.

It supports:
- ✅ College FAQ matching using fuzzy logic
- 🤖 Open-ended responses using T5 (fine-tuned)
- 🧠 Chat memory (context-aware replies)
- 📄 PDF download of chat history
- 🌐 Deployment-ready on Streamlit Cloud

## 🏗️ Tech Stack

- Python
- Streamlit
- Hugging Face Transformers (T5)
- FuzzyWuzzy for FAQ matching
- FPDF for PDF export

## 🚀 Run Locally

```bash
git clone https://github.com/Shubam081220/College_chatbot.git
cd College_chatbot
pip install -r requirements.txt
streamlit run frontend/app.py
 
=======
# College Chatbot

An intelligent chatbot for college-related queries, built using Streamlit and fine-tuned T5 model. It supports both open-ended question answering and FAQ-style fallback responses using fuzzy matching.

# Features

-  Answer open-ended questions using a fine-tuned T5 model
-  Fuzzy-matching for college FAQs
-  Streamlit-based interactive UI
-  Planned support for chat history context memory
-  PDF export for chat responses (coming soon)

# Getting Started

# Clone the repo
git clone https://github.com/Shubam081220/College_chatbot.git

# Create and activate a virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate   # On Windows

# Install dependencies
pip install -r requirements.txt

# Run the model on streamlit
streamlit run chatbot.py
>>>>>>> 3578a29edd060ca02c5930fe84f03640c4be4aea
