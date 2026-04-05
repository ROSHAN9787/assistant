import pickle
import re

with open("intent_model.pkl", "rb") as f:
    vectorizer, model = pickle.load(f)

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)

    remove_words = [
        "please", "tell me", "can you",
        "right now", "now",
        "who is", "what is", "about",
        "the", "of"
    ]
    for w in remove_words:
        text = text.replace(w, "")
    return text.strip()

def predict_intent(text):
    text = clean_text(text)
    vec = vectorizer.transform([text])

    # probability check
    probs = model.predict_proba(vec)[0]
    max_prob = max(probs)

    if max_prob < 0.35:
        return None

    return model.classes_[probs.argmax()]
