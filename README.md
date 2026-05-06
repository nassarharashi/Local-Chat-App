# Local Chat App

A simple ChatGPT-style chat app built with Streamlit and Python. It uses `st.chat_message` and `st.chat_input` to create a conversational UI, and it stores the conversation in `st.session_state.messages` so the chat history stays visible while you talk.

This project does **not** use any external LLM or API. Responses are generated locally with a small Python function.

## Features

- ChatGPT-like interface built with Streamlit
- Local, rule-based mock assistant replies
- Conversation history kept in session state
- Clear chat button in the sidebar
- Single-file app structure

## Requirements

- Python 3.13+
- Streamlit

## Installation

Install Streamlit if you have not already:

```powershell
pip install streamlit
```

## Run the App

From the project folder, run:

```powershell
streamlit run chat_app.py
```

## How It Works

- The app checks `st.session_state.messages` when it starts.
- If no history exists, it adds a default assistant greeting.
- Each user message is appended to the session state.
- A local Python function generates a mock assistant reply.
- The assistant response is also stored in session state and shown in the chat UI.

## File Structure

- `chat_app.py` - main Streamlit application
- `README.md` - project overview and setup instructions

## Notes

- No external APIs are used.
- No LLM model is required.
- The app is designed for demonstrating Streamlit basics and simple state management.
