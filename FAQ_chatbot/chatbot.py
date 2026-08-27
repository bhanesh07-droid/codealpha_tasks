
import json
import re
from pathlib import Path
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DATA_PATH = Path(__file__).with_name("faq_data.json")

def clean(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

with open(DATA_PATH, encoding="utf-8") as f:
    FAQS = json.load(f)

questions = [clean(x["question"]) for x in FAQS]
vectorizer = TfidfVectorizer(ngram_range=(1,2), stop_words="english")
matrix = vectorizer.fit_transform(questions)

def answer_question(user_question, threshold=0.25):
    q = vectorizer.transform([clean(user_question)])
    scores = cosine_similarity(q, matrix)[0]
    idx = int(np.argmax(scores))
    score = float(scores[idx])
    if score < threshold:
        return "I couldn't find a reliable FAQ match. Please rephrase your question.", score, None
    return FAQS[idx]["answer"], score, FAQS[idx]["question"]

if __name__ == "__main__":
    print("CodeAlpha FAQ Chatbot — type 'quit' to exit.")
    while True:
        q = input("\nYou: ").strip()
        if q.lower() in {"quit", "exit"}:
            break
        ans, score, matched = answer_question(q)
        print(f"Bot: {ans}")
        print(f"(similarity={score:.3f}, matched={matched})")
