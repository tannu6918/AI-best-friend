import streamlit as st
import openai

st.title("AI Best Friend")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Say something…"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("assistant"):
        st.markdown("...")

import random, time

def response_generator():
    resp = random.choice([
        "Hi there! 😊 What’s on your mind today?",
        "I’m here for you!",
        "Tell me more…"
    ])
    for w in resp.split():
        yield w + " "
        time.sleep(0.05)


with st.chat_message("assistant"):
    response = st.write_stream(response_generator())
    st.session_state.messages.append({"role": "assistant", "content": response})



openai.api_key = st.secrets["OPENAI_API_KEY"]

def response_generator():
    resp = openai.ChatCompletion.create(
        model="gpt‑3.5‑turbo",
        messages=[{"role":"user","content": prompt}],
        stream=True
    )
    for chunk in resp:
        yield chunk.choices[0].delta.content
