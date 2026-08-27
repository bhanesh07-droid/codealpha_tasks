# Task 2 Explanation

### Pipeline
User question → cleaning → TF-IDF vectorization → cosine similarity → best FAQ → threshold check → response

### Why cosine similarity?
It compares the direction of the TF-IDF vectors, making it suitable for matching semantically related FAQ wording when the FAQ set is small.

### Extension ideas
- Add intent classification
- Use sentence embeddings
- Add conversation memory
- Connect FAQs to a database
- Add multilingual support
