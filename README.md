# Podcast Summarizer (PodSumm)

Podcast Summarizer is a tool that leverages the Whisper ASR model and GPT-3.5 Turbo to generate concise summaries of podcast episodes. This repository contains the source code and resources needed to use and integrate it.

## Features

- **Whisper ASR Integration:** Utilizes the optimised version of Whisper ASR (Automatic Speech Recognition) model by [Sanchit Gandhi](https://github.com/sanchit-gandhi/whisper-jax) for accurate transcription of podcast audio.
- **GPT-3.5 Turbo for Summarization:** Leverages the GPT-3.5 Turbo language model to generate summaries.
- **Customizable Configuration:** The summarization process is customizable by changing the prompts given to model.
- **PyTube:** The python library for downloading and extracting the audio stream from the YouTube videos.

## Installation

- Clone the repository to your environment using terminal or CLI.
- Run `pip install -r requirements.txt` to install the dependencies. 
- Run `sudo apt-get -r packages.txt` to install the packages. (for Linux)
- More information about downloading ``ffmpeg`` package can be refered [here.](https://ffmpeg.org/download.html) 

## Usage

- To run the application locally run ``streamlit run app.py`` to launch the web application.
- It is also deployed as a web-applicaiton which can be accessed [here.](https://pod-summ.streamlit.app/)

## Limitations

- It takes time for transcribing the videos. 

## Future work

- To implement a feature to analyse the sentiment of the speakers in the podcast.
