# AI Best Friend

A ChatGPT‑style web app built with Streamlit and OpenAI’s GPT API, featuring a fun “AI Best Friend” interface.

# Features
1. Real-time streaming responses via st.write_stream()

2.Chat history management using st.session_state

3.Easy-to-use UI leveraging st.chat_message() and st.chat_input()

4.Supports both mock responses and actual OpenAI API calls

5.Simple cool design—emoji responses, typing effect animation

# Requirements

streamlit>=1.28
openai>=0.27

# Setup
 1. #### Clone the repo:


git clone <https://github.com/tannu6918/AI-best-friend.git>

 2. #### Install dependencies:

bash

pip install -r streamlit

3. #### Add your OpenAI key in .streamlit/secrets.toml:

toml
OPENAI_API_KEY = "sk-KEY"

# How It Works
1.Session state initializes messages = []

2. Each chat run:

Displays history with st.chat_message()

Captures the user prompt via st.chat_input()

3.Streaming response:


Shows animated text from random.choice fallback







 # Running the App
bash
Copy
edit
streamlit run your_app.py





