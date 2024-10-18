# transcription.py
from google.cloud import speech_v1p1beta1 as speech

def transcribe_video(video_file):
    client = speech.SpeechClient()
    audio = speech.RecognitionAudio(content=video_file.read())
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code="en-US",
    )
    response = client.recognize(config=config, audio=audio)
    return response.results[0].alternatives[0].transcript