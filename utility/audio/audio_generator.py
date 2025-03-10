import edge_tts
import asyncio

async def generate_audio(text: str, output_file: str = "audio_tts.wav") -> str:
    communicate = edge_tts.Communicate(text, voice="en-US-JennyNeural")
    await communicate.save(output_file)
    return output_file

def generate_audio_sync(text: str) -> str:
    return asyncio.run(generate_audio(text))
