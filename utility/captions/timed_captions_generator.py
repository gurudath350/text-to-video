import whisper_timestamped as whisper

def generate_timed_captions(audio_file: str) -> list:
    model = whisper.load_model("base")
    result = whisper.transcribe(model, audio_file, language="en")
    
    timed_captions = []
    for segment in result["segments"]:
        start = segment["start"]
        end = segment["end"]
        text = segment["text"].strip()
        timed_captions.append((start, end, text))
    
    return timed_captions
