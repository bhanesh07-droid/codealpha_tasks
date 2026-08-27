
import streamlit as st
from chatbot import answer_question

st.set_page_config(page_title="FAQ Chatbot", page_icon="💬")
st.title("💬 AI FAQ Chatbot")
st.caption("TF-IDF + cosine similarity")

if "messages" not in st.session_state:
    st.session_state.messages = []

for role, msg in st.session_state.messages:
    with st.chat_message(role):
        st.write(msg)

q = st.chat_input("Ask a question…")
if q:
    st.session_state.messages.append(("user", q))
    ans, score, matched = answer_question(q)
    response = ans + f"\n\nSimilarity: {score:.2f}"
    if matched:
        response += f"\nMatched FAQ: {matched}"
    st.session_state.messages.append(("assistant", response))
    st.rerun()
