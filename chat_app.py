import random
import time
from typing import Dict, List

import streamlit as st


st.set_page_config(page_title="Local Chat", page_icon="💬", layout="centered")

st.title("Local Chat")
st.caption("Chat demo using Streamlit session state. No external APIs or LLMs.")


def generate_mock_reply(user_text: str) -> str:
    """Generate a local reply based on simple rules."""
    text = user_text.strip()
    lower_text = text.lower()

    rules = {
        "hello": "Hello! How can I help you today?",
        "hi": "Hi there! What would you like to talk about?",
        "help": "I can echo your message and show how local replies work.",
        "thanks": "You're welcome!",
        "bye": "Goodbye!",
    }

    for key, value in rules.items():
        if key in lower_text:
            return value

    templates = [
        "Got it. You said: '{text}'.",
        "Thanks for sharing: '{text}'.",
        "I hear you. Your message was: '{text}'.",
        "Understood. Here is a local echo: '{text}'.",
    ]
    return random.choice(templates).format(text=text)


def init_messages() -> None:
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Hi! Ask me anything and I'll respond locally.",
            }
        ]


def render_messages(messages: List[Dict[str, str]]) -> None:
    for message in messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


def append_message(role: str, content: str) -> None:
    st.session_state.messages.append({"role": role, "content": content})


init_messages()

with st.sidebar:
    if st.button("Clear chat", use_container_width=True):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Chat cleared. Ask me anything and I'll respond locally.",
            }
        ]


render_messages(st.session_state.messages)

user_prompt = st.chat_input("Type a message...")
if user_prompt:
    append_message("user", user_prompt)
    with st.chat_message("user"):
        st.markdown(user_prompt)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        reply = generate_mock_reply(user_prompt)
        for i in range(1, len(reply) + 1):
            placeholder.markdown(reply[:i])
            time.sleep(0.01)

    append_message("assistant", reply)
