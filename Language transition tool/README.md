# CodeAlpha Task 1 — Language Translation Tool

## Requirements implemented
- Text input UI
- Source and target language selection
- Translation API integration
- Clear translated output
- Copy/download result
- Google Cloud Translation v3 support
- Optional LibreTranslate fallback

## Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

### Google Cloud setup
Set `GOOGLE_CLOUD_PROJECT` and configure Google Application Default Credentials.

Google's current Cloud Translation documentation uses the Python `google.cloud.translate_v3` client and a `projects/.../locations/global` parent for `translate_text`.

### Alternative
Set `LIBRETRANSLATE_URL` and optionally `LIBRETRANSLATE_API_KEY`, then choose LibreTranslate in the UI.

Do not commit API keys or credentials to GitHub.
