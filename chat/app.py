import streamlit as st
import requests
import json

#page config
st.set_page_config(
    page_title="ai assistant demo",
    layout="wide"
)

st.markdown("""
    <style>
    .main {
        background-color: white;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .user-message {
        background-color: #f8f9fa;
    }
    .assistant-message {
        background-color: #ffffff;
        border-left: 3px solid #4CAF50;
    }
    </style>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

def get_ollama_response(prompt, conversation_history):
    url = "http://localhost:11434/api/generate"
    
    context = ""
    for msg in conversation_history:
        role = "User" if msg["role"] == "user" else "Assistant"
        context += f"{role}: {msg['content']}\n"
    
    full_prompt = context + f"User: {prompt}\nAssistant:"
    
    payload = {
        "model": "gemma3:1b",
        "prompt": full_prompt,
        "stream": False
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()["response"]
    except requests.exceptions.ConnectionError:
        return "error!, ollama model not pulled, make sure use gemma3:1b models, or ollama not serve, check error log."
    except Exception as e:
        return f"Error: {str(e)}"


st.title("ai chat assistant")
st.markdown("---")

#message display
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"<div class='chat-message user-message'><b>You:</b> {message['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-message assistant-message'><b>Assistant:</b> {message['content']}</div>", unsafe_allow_html=True)

#input
user_input = st.chat_input("ask question...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.spinner("thinking..."):
        response = get_ollama_response(user_input, st.session_state.messages[:-1])
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()

#sidebar
with st.sidebar:
    st.markdown("About!")
    st.markdown("Chat assistant with google's gemma3:1b models")
    
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("demo usage")