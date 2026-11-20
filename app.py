
import streamlit as st
from deep_translator import MyMemoryTranslator
from langdetect import detect, LangDetectException

st.set_page_config(
    page_title="JARVIS Translation Tool",
    page_icon="🌐",
    layout="centered"
)

st.title("🌐 JARVIS Translation Tool")
st.subheader("Smart Language Translation")
st.write("Translate text between multiple languages easily.")

LANGUAGES = {
    "English": "en-GB",
    "Hindi": "hi-IN",
    "French": "fr-FR",
    "German": "de-DE",
    "Spanish": "es-ES",
    "Japanese": "ja-JP",
    "Chinese": "zh-CN",
    "Arabic": "ar-SA",
    "Bengali": "bn-IN",
    "Tamil": "ta-IN",
    "Telugu": "te-IN",
    "Portuguese": "pt-PT",
    "Russian": "ru-RU",
    "Italian": "it-IT",
    "Korean": "ko-KR",
    "Urdu": "ur-PK"
}

DETECTED_CODES = {
    "en": "en-GB",
    "hi": "hi-IN",
    "fr": "fr-FR",
    "de": "de-DE",
    "es": "es-ES",
    "ja": "ja-JP",
    "zh-cn": "zh-CN",
    "ar": "ar-SA",
    "bn": "bn-IN",
    "ta": "ta-IN",
    "te": "te-IN",
    "pt": "pt-PT",
    "ru": "ru-RU",
    "it": "it-IT",
    "ko": "ko-KR",
    "ur": "ur-PK"
}

text = st.text_area(
    "Enter your text",
    placeholder="Type text here...",
    height=150
)

col1, col2 = st.columns(2)

with col1:
    source = st.selectbox(
        "Source Language",
        ["Auto Detect"] + list(LANGUAGES.keys())
    )

with col2:
    target = st.selectbox(
        "Target Language",
        list(LANGUAGES.keys()),
        index=1
    )

if st.button("Translate 🌐", use_container_width=True):

    if not text.strip():
        st.warning("Please enter some text.")

    else:
        try:
            if source == "Auto Detect":
                detected = detect(text)
                source_code = DETECTED_CODES.get(detected)

                if not source_code:
                    st.error(
                        "Detected language is not supported. "
                        "Please select the source language manually."
                    )
                    st.stop()
            else:
                source_code = LANGUAGES[source]

            target_code = LANGUAGES[target]

            if source_code == target_code:
                st.info("Both languages are the same.")

            else:
                with st.spinner("Translating..."):
                    translator = MyMemoryTranslator(
                        source=source_code,
                        target=target_code
                    )
                    result = translator.translate(text)

                if result:
                    st.success("Translation completed!")

                    st.subheader("Translated Text")
                    st.text_area(
                        "Translation Result",
                        value=result,
                        height=150
                    )

                    st.download_button(
                        label="Download Translation",
                        data=result,
                        file_name="translated_text.txt",
                        mime="text/plain"
                    )

                else:
                    st.error("No translation received. Please try again.")

        except LangDetectException:
            st.error(
                "Could not detect the language. "
                "Please select it manually."
            )

        except Exception as error:
            st.error("Translation failed. Please try again later.")
            st.caption(f"Error details: {error}")

st.divider()
st.caption("JARVIS Translation Tool | CodeAlpha Internship Project")
