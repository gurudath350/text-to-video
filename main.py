import os
from dotenv import load_dotenv
from utility.script.script_generator import generate_script
from utility.audio.audio_generator import generate_audio
from utility.captions.timed_captions_generator import generate_timed_captions
from utility.video.video_search_query_generator import get_video_search_queries_timed
from utility.video.background_video_generator import generate_video_url
from utility.render.render_engine import get_output_media

load_dotenv()

def main():
    topic = "The Science of Black Holes"
    
    # Generate script
    script = generate_script(topic)
    print("✅ Script Generated")
    
    # Generate audio
    audio_file = generate_audio(script["script"])
    print(f"✅ Audio Saved to {audio_file}")
    
    # Generate timed captions
    timed_captions = generate_timed_captions(audio_file)
    print("✅ Timed Captions Generated")
    
    # Generate video search queries
    search_queries = get_video_search_queries_timed(script["script"], timed_captions)
    print("✅ Video Search Queries Generated")
    
    # Fetch background videos
    video_urls = generate_video_url(search_queries)
    print("✅ Background Videos Fetched")
    
    # Render final video
    output_video = get_output_media(audio_file, timed_captions, video_urls)
    print(f"✅ Video Rendered: {output_video}")

if __name__ == "__main__":
    main()
