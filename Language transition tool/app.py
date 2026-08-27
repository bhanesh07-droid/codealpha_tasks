
import os
import html
import streamlit as st

st.set_page_config(page_title="AI Language Translation Tool", page_icon="🌍", layout="centered")

LANGUAGES = {
    "English": "en", "Hindi": "hi", "Kannada": "kn", "Tamil": "ta",
    "Telugu": "te", "Malayalam": "ml", "Marathi": "mr", "Bengali": "bn",
    "Gujarati": "gu", "Punjabi": "pa", "French": "fr", "German": "de",
    "Spanish": "es", "Italian": "it", "Portuguese": "pt", "Japanese": "ja",
    "Korean": "ko", "Chinese": "zh", "Arabic": "ar", "Russian": "ru"
}

def google_translate_v3(text, source, target):
    """Google Cloud Translation v3 using Application Default Credentials."""
    from google.cloud import translate_v3
    project_id = os.environ["GOOGLE_CLOUD_PROJECT"]
    client = translate_v3.TranslationServiceClient()
    parent = f"projects/{project_id}/locations/global"
    response = client.translate_text(
        request={
            "contents": [text],
            "mime_type": "text/plain",
            "source_language_code": source,
            "target_language_code": target,
            "parent": parent,
        }
    )
    return response.translations[0].translated_text

def libretranslate(text, source, target):
    """Optional fallback for a self-hosted/public LibreTranslate endpoint."""
    import requests
    endpoint = os.getenv("LIBRETRANSLATE_URL", "https://libretranslate.com/translate")
    payload = {"q": text, "source": source, "target": target, "format": "text"}
    api_key = os.getenv("LIBRETRANSLATE_API_KEY")
    if api_key:
        payload["api_key"] = api_key
    r = requests.post(endpoint, data=payload, timeout=30)
    r.raise_for_status()
    return r.json()["translatedText"]

st.title("🌍 AI Language Translation Tool")
st.caption("CodeAlpha Artificial Intelligence — Task 1")

text = st.text_area("Enter text", height=160, placeholder="Type the text you want to translate…")
c1, c2 = st.columns(2)
with c1:
    source_name = st.selectbox("Source language", list(LANGUAGES), index=0)
with c2:
    target_name = st.selectbox("Target language", list(LANGUAGES), index=2)

provider = st.radio("Translation provider", ["Google Cloud Translation", "LibreTranslate"], horizontal=True)

if st.button("Translate", type="primary", use_container_width=True):
    if not text.strip():
        st.warning("Please enter some text.")
    elif source_name == target_name:
        st.info("Source and target languages are the same.")
        st.text_area("Translated text", value=text, height=160)
    else:
        try:
            if provider.startswith("Google"):
                result = google_translate_v3(text, LANGUAGES[source_name], LANGUAGES[target_name])
            else:
                result = libretranslate(text, LANGUAGES[source_name], LANGUAGES[target_name])
            st.session_state["translation"] = result
        except Exception as exc:
            st.error("Translation failed. Check your API credentials/network settings.")
            st.exception(exc)

if "translation" in st.session_state:
    st.subheader("Translated text")
    st.text_area("Result", value=st.session_state["translation"], height=160)
    st.download_button(
        "Copy / Download result",
        data=st.session_state["translation"],
        file_name="translation.txt",
        mime="text/plain",
        use_container_width=True,
    )
