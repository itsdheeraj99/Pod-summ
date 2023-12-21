import streamlit as st
import os
from pytube import YouTube
from pathlib import Path
from whisper_jax import FlaxWhisperPipline
import openai

# Set your OpenAI API key
openai.api_key = ""

# Function to get completion from OpenAI GPT-3.5 Turbo
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    response_message = response.choices[0].message.content
    return response_message

# Function to transcribe audio using Whisper
@st.cache_resource
def transcription(audio_file):
    model = FlaxWhisperPipline("openai/whisper-base")
    outputs = model(audio_file,  task="transcribe", return_timestamps=False)
    return outputs['text']

# Function to save audio from YouTube URL
def save_audio(url):
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    file_name = yt.title + ".mp3"
    output_path = "Youtube_dl"
    out_file = audio_stream.download(output_path=output_path, filename=file_name)
    try:
        os.rename(out_file, file_name)
    except WindowsError:
        os.remove(file_name)
        os.rename(out_file, file_name)
    audio_filename = Path(file_name).stem + '.mp3'
    thumbnail_url = yt.thumbnail_url
    return audio_filename, thumbnail_url

# Streamlit app
def main():
    st.title("PodSumm")

    # Input for YouTube URL
    url = st.text_input("Enter the YouTube video URL:")

    if st.button("Transcribe"):
        # Save audio from YouTube URL
        audio_filename, thumbnail_url = save_audio(url)

        # Transcribe audio
        transcript = transcription(audio_filename)

        # Generate prompt for OpenAI GPT-3.5 Turbo
        prompt = f''' Extract key takeaways from the following transcript and print them out in the following manner:
        1.
        2.
        3.
        4.
        5.
        Transcript: {transcript}
        '''

        # Get completion from OpenAI
        summary = get_completion(prompt)

        # Create two columns
        col1, col2 = st.columns(2)

        # Display the video thumbnail in the first column
        col1.image(thumbnail_url, caption='Video Thumbnail', use_column_width=True)

        # Display the key takeaways in the second column
        col2.subheader("Key Takeaways")
        col2.text(summary)

        

if __name__ == "__main__":
    main()
