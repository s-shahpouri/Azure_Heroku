import streamlit as st
import azure.cognitiveservices.speech as speechsdk
import pydub
from PIL import Image
import traceback
import time
from dotenv import load_dotenv
import os


# Page Configuration
st.set_page_config(
    page_title="Speech-to-Text Web App",
    page_icon="🎧",
    layout="wide",
)

st.markdown(
    """
    <style>
    .main-header {
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
        color: #620E8A;
    }
    .sub-header {
        font-size: 14px;
        text-align: center;
        margin-bottom: 20px;
        color: #555;
    }

    .image {
        justify-content: center;
        text-align: center;

    }
    footer {visibility: hidden;}
    </style>
    <div class="main-header">Speech-to-Text Web App</div>
    <div class="sub-header">Transcribe audio files with Azure Speech SDK</div>
    """,
    unsafe_allow_html=True,
)



load_dotenv()
azure_key = os.getenv("AZURE_SPEECH_KEY")
print("SDGDFGDFG")
print(azure_key)

def speech_recognize_from_file(sound, selected_language):
    speech_config = speechsdk.SpeechConfig(subscription=azure_key, region="westeurope")
    audio_config = speechsdk.audio.AudioConfig(filename=sound)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, language=selected_language, audio_config=audio_config)

    result = speech_recognizer.recognize_once()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return result.text

    elif result.reason == speechsdk.ResultReason.NoMatch:
        return "No Speech Recognized: {}".format(result.no_match_details)

    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            return "Speech Recognition canceled due to error: {}".format(cancellation_details.error_details)
        return "Speech Recognition canceled: {}".format(cancellation_details.reason)


image = Image.open('./1.png')
st.image(image)

col1, col2 = st.columns([1, 2])
with col1:
    # st.markdown("Select Language")
    language_options = {
        "English (US)": "en-US",
        "French (FR)": "fr-FR",
        "Spanish (ES)": "es-ES",
        "German (DE)": "de-DE",
        "Chinese (Mandarin)": "zh-CN"
    }
    selected_language = st.selectbox("Choose the language", list(language_options.keys()))

with col2:
    # st.markdown("Upload Your Audio File")
    uploaded_file = st.file_uploader("Choose a WAV file", type=["wav"])

if uploaded_file:
    with open("temp_audio.wav", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.audio(uploaded_file, format="audio/wav")

    # Transcription Process
    if st.button("Transcribe Audio"):
        with st.spinner("Transcribing..."):
            transcription = speech_recognize_from_file("temp_audio.wav", language_options[selected_language])
            if transcription:
                st.success("Transcription Completed!")
                st.text_area("Transcribed Text", transcription, height=200)

                # Save Transcription History
                with open("transcription_history.txt", "a") as history_file:
                    history_file.write(f"File: {uploaded_file.name}\nLanguage: {selected_language}\nTranscription: {transcription}\n---\n")

                # Export Transcription
                st.download_button(
                    label="Download Transcription as Text File",
                    data=transcription,
                    file_name="transcription.txt",
                    mime="text/plain",
                )
            else:
                st.error("Transcription failed. Please try again.")

# Footer Section
st.caption(
    """
    <style>
    .footer {
        text-align: center;
        font-size: 14px;
        margin-top: 50px;
        color: #888;
    }
    </style>
    <div class="footer">
        Created with ❤️ by <a href="https://github.com/s-shahpouri" target="_blank">Sama</a><br>
        This app uses <a href="https://ai.azure.com/explore/aiservices/speech" target="_blank">Azure Speech-to-Text SDK</a> to transcribe audio files into text.<br>
        It is built with <a href="https://www.python.org" target="_blank">Python</a> and deployed on <a href="https://www.heroku.com" target="_blank">Heroku</a>, hosted on <a href="https://streamlit.io" target="_blank">Streamlit</a>.<br>
    </div>
    """,
    unsafe_allow_html=True,
)