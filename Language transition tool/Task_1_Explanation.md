# Task 1 Explanation

### Architecture
User → Streamlit UI → Translation Provider → Translated Text → Display/Download

### AI component
The actual language translation is performed by the selected machine-translation API. The application handles input, language selection, API communication, error handling and presentation.

### Demonstration flow
1. Enter English text.
2. Select English → Kannada (or another pair).
3. Click Translate.
4. The API returns the translated text.
5. The result is displayed and can be downloaded.
