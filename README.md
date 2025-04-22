# 🤖 Q&A Chatbot with OpenAI & Langchain

Welcome to the **Q&A Chatbot** powered by **OpenAI** and built with **Streamlit**, **Langchain**, and **Python**. This chatbot can answer your questions in a conversational style using state-of-the-art LLMs like GPT-4.

---

## 🚀 Demo

👉 [Click here to try the live app](https://your-streamlit-app-url)  
*(Replace with your Streamlit Cloud URL)*

---

## 🧠 Features

- 🔒 Secure OpenAI API key integration
- 🔄 Real-time Q&A with GPT-4, GPT-4-turbo, GPT-4o
- 🧠 Powered by Langchain and OpenAI models
- 🎛 Customizable settings: temperature, token limit, model selection
- 🌐 Deployed on Streamlit Cloud

---

## 🛠 Tech Stack

- [Streamlit](https://streamlit.io/)
- [OpenAI API](https://platform.openai.com/)
- [Langchain](https://www.langchain.com/)
- [Python](https://www.python.org/)
- [Dotenv](https://pypi.org/project/python-dotenv/)

---

## 📦 Installation

1. **Clone the repo**

```bash
git clone https://github.com/your-username/qna-chatbot-openai.git
cd qna-chatbot-openai
python -m venv venv
source venv/bin/activate     # On Mac/Linux
venv\Scripts\activate        # On Windows

pip install -r requirements.txt

OPENAI_API_KEY=your_openai_api_key
LANGCHAIN_API_KEY=your_langchain_api_key

streamlit run app.py
