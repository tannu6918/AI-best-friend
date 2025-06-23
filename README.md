# AI Best Friend

## A ChatGPT‑style web app built with Streamlit and OpenAI’s GPT API, featuring a fun “AI Best Friend” interface.

# Features
1. Real-time streaming responses via st.write_stream()

Chat history management using st.session_state

Easy-to-use UI leveraging st.chat_message() and st.chat_input()

Supports both mock responses and actual OpenAI API calls

Simple cool design—emoji responses, typing effect animation

📋 #Requirements
txt
Copy
Edit
streamlit>=1.28
openai>=0.27
🔧 Setup
Clone the repo:

bash
Copy
Edit
git clone <your-repo-url>
cd <your-repo-folder>
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Add your OpenAI key in .streamlit/secrets.toml:

toml
Copy
Edit
OPENAI_API_KEY = "sk-KEY"
🧩 How It Works
Session state initializes messages = []

Each chat run:

Displays history with st.chat_message()

Captures the user prompt via st.chat_input()

Streaming response:

Shows animated text from random.choice fallback

Or streams from OpenAI model:

python
Copy
Edit
stream = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[...],
  stream=True
)
response = st.write_stream(stream)
st.session_state.messages.append({"role": "assistant", "content": response})
Conversation persists between reruns 🎉

Adapted from Streamlit's official “ChatGPT‑like clone” tutorial 
reddit.com
+10
docs.streamlit.io
+10
github.com
+10
github.com
+1
github.com
+1
github.com
github.com
+11
github.com
+11
reddit.com
+11
.

🛠️ Running the App
bash
Copy
Edit
streamlit run your_app.py
📝 Example README Template
You can base your GitHub README on this layout:

markdown
Copy
Edit
# AI Best Friend

## Features
- Streaming chat UI
- Emoji‑rich interaction
- Switch between fun mode and GPT mode

## Setup
```bash
pip install -r requirements.txt
Usage
Set your OpenAI key in .streamlit/secrets.toml

Run streamlit run your_app.py

Code Explained
session_state holds chat history

st.chat_input() for input

Two modes: random-mock and OpenAI stream


