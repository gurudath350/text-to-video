from moviepy.editor import (
    VideoFileClip,
    AudioFileClip,
    TextClip,
    CompositeVideoClip,
)
from typing import List, Tuple

def get_output_media(
    audio_file: str,
    timed_captions: List[Tuple[float, float, str]],
    video_urls: List[Tuple[float, float, str]],
    output_file: str = "output.mp4",
) -> str:
    audio = AudioFileClip(audio_file)
    video_clips = []
    
    for start, end, url in video_urls:
        clip = VideoFileClip(url).subclip(start, end)
        video_clips.append(clip)
    
    final_clip = CompositeVideoClip(video_clips)
    final_clip = final_clip.set_audio(audio)
    
    for start, end, text in timed_captions:
        txt_clip = (
            TextClip(text, fontsize=24, color="white")
            .set_position(("center", "bottom"))
            .set_duration(end - start)
            .set_start(start)
        )
        final_clip = CompositeVideoClip([final_clip, txt_clip])
    
    final_clip.write_videofile(output_file, fps=24)
    return output_file
