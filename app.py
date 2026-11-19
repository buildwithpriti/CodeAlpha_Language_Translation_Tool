import io

import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS, lang as gtts_lang

st.set_page_config(page_title="Language Translation Tool", page_icon="🌐")
st.title("🌐 Language Translation Tool")
st.caption("CodeAlpha AI Internship - Task 1")


@st.cache_data
def get_languages():
    # {"english": "en", "hindi": "hi", ...}
    return GoogleTranslator().get_supported_languages(as_dict=True)


languages = get_languages()
names = sorted(languages.keys())

col1, col2, col3 = st.columns([5, 1, 5])
with col1:
    src_name = st.selectbox(
        "From", ["auto detect"] + names, index=0
    )
with col2:
    st.write("")
    st.write("")
    st.markdown("### ➜")
with col3:
    tgt_name = st.selectbox("To", names, index=names.index("hindi"))

text = st.text_area("Enter text", height=160, max_chars=5000,
                    placeholder="Type or paste text here...")

if st.button("Translate", type="primary"):
    if not text.strip():
        st.warning("Please enter some text first.")
    else:
        src_code = "auto" if src_name == "auto detect" else languages[src_name]
        tgt_code = languages[tgt_name]
        try:
            with st.spinner("Translating..."):
                result = GoogleTranslator(source=src_code, target=tgt_code).translate(text)
            st.session_state["result"] = result
            st.session_state["tgt_code"] = tgt_code
        except Exception as e:
            st.error(f"Translation failed: {e}")

if "result" in st.session_state:
    st.subheader("Translation")
    # st.code shows a built-in copy button at the top-right
    st.code(st.session_state["result"], language=None, wrap_lines=True)

    if st.button("🔊 Listen"):
        code = st.session_state["tgt_code"]
        if code not in gtts_lang.tts_langs():
            st.info("Text-to-speech is not available for this language.")
        else:
            try:
                audio = io.BytesIO()
                gTTS(st.session_state["result"], lang=code).write_to_fp(audio)
                st.audio(audio.getvalue(), format="audio/mp3")
            except Exception as e:
                st.error(f"Could not generate audio: {e}")
