# CodeAlpha Task 2 — Chatbot for FAQs

## Requirements implemented
- FAQ question/answer dataset
- Text preprocessing
- TF-IDF vectorization
- Cosine similarity
- Best FAQ matching
- Confidence/similarity threshold
- Command-line chatbot
- Streamlit chat UI

## Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

The matching system is intentionally transparent: the user's question is transformed into TF-IDF features and compared with the stored FAQ questions using cosine similarity.
