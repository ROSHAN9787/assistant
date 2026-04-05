import streamlit as st
from textblob import TextBlob
import random

# ---------- Crisis Keywords ----------
CRISIS_WORDS = [
    "suicide", "kill myself", "end my life",
    "self harm", "die", "hopeless"
]

# ---------- Coping Strategies ----------
COPING_STRATEGIES = [
    "Try slow deep breathing for 1 minute 🌬️",
    "Write down your thoughts 📝",
    "Listen to calm music 🎵",
    "Take a short walk 🚶‍♀️",
    "Talk to someone you trust ❤️"
]

# ---------- Responses ----------
RESPONSES = {
    "positive": [
        "I'm really glad to hear that 😊",
        "That sounds positive! Tell me more 💬"
    ],
    "neutral": [
        "I’m here to listen 🙂",
        "Please share more if you feel comfortable."
    ],
    "negative": [
        "I'm really sorry you're feeling this way 💙",
        "That sounds difficult. You’re not alone 🤍"
    ]
}

# ---------- Emotion Detection ----------
def detect_emotion(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.2:
        return "positive"
    elif polarity < -0.2:
        return "negative"
    else:
        return "neutral"

# ---------- Crisis Detection ----------
def check_crisis(text):
    text = text.lower()
    return any(word in text for word in CRISIS_WORDS)

# ---------- AI Response ----------
def generate_response(user_input):
    if check_crisis(user_input):
        return (
            "💔 **I'm really sorry you're feeling this much pain.**\n\n"
            "**Please reach out immediately:**\n"
            "- A trusted friend or family member\n"
            "- A mental health professional\n"
            "- Local emergency helpline\n\n"
            "❤️ **Your life matters. You are not alone.**"
        )

    emotion = detect_emotion(user_input)
    reply = random.choice(RESPONSES[emotion])

    if emotion == "negative":
        reply += f"\n\n💡 **Suggestion:** {random.choice(COPING_STRATEGIES)}"

    return reply

# ---------- Streamlit UI ----------
st.set_page_config(page_title="AI Mental Health Companion", page_icon="🧠")

st.title("🧠 AI Mental Health Companion")
st.write("⚠️ *This is not a medical professional. It provides emotional support only.*")

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("How are you feeling today?")

if st.button("Send"):
    if user_input.strip() != "":
        response = generate_response(user_input)
        st.session_state.chat.append(("You", user_input))
        st.session_state.chat.append(("AI", response))

# ---------- Display Chat ----------
for sender, msg in st.session_state.chat:
    if sender == "You":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown(f"**🤖 AI:** {msg}")
