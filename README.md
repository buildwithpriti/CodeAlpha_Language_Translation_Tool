# CodeAlpha_Translation_Tool

Language translation web app built for the **CodeAlpha AI Internship (Task 1)**.

## Features
- Enter text, choose source (or auto-detect) and target language
- Translation through the Google Translate API (via `deep-translator`)
- Clear output display with one-click **copy** button
- **Text-to-speech** for the translated text (gTTS)

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Tech stack
Python, Streamlit, deep-translator, gTTS
