import streamlit as st
from services.chatbot_service import ChatbotService

st.set_page_config(page_title="AI Career Advisor", layout="centered")

st.title("🎯 AI Career Advisor Chatbot")
st.caption("Powered by Google Gemini")

if "chatbot" not in st.session_state:
    st.session_state.chatbot = ChatbotService()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Ask about careers, skills, resume, interview prep...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.chatbot.get_response(user_input)
            st.write(response)

    st.session_state.messages.append({"role": "assistant", "content": response})