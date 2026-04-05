import json
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

with open("intents.json", "r") as f:
    data = json.load(f)

texts = []
labels = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        texts.append(pattern)
        labels.append(intent["tag"])

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = LogisticRegression(max_iter=1000)
model.fit(X, labels)

with open("intent_model.pkl", "wb") as f:
    pickle.dump((vectorizer, model), f)

print("Training complete")
