# video_processor.py
from transcription import transcribe_video
from text_correction import correct_text
from text_to_speech import text_to_speech
from audio_sync import sync_audio_with_video

def process_video(video_file):
    transcript = transcribe_video(video_file)
    corrected_text = correct_text(transcript)
    new_audio = text_to_speech(corrected_text)
    final_video = sync_audio_with_video(video_file, new_audio)
    return final_video