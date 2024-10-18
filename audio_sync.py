# audio_sync.py
from moviepy.editor import VideoFileClip, AudioFileClip

def sync_audio_with_video(video_path, audio_path):
    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path)
    final_clip = video.set_audio(audio)
    return final_clip