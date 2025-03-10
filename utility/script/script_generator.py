import os
from openrouter import OpenRouter
from dotenv import load_dotenv

load_dotenv()

def generate_script(topic: str) -> dict:
    client = OpenRouter(api_key=os.getenv("OPENROUTER_API_KEY"))
    
    response = client.chat.completions.create(
        model="qwen/qwq-32b:free",
        messages=[
            {
                "role": "system",
                "content": "You are a YouTube Shorts scriptwriter. Generate a 60-second script with timestamps and visual cues.",
            },
            {"role": "user", "content": f"Topic: {topic}"},
        ],
        temperature=0.7,
        max_tokens=512,
    )
    
    return {
        "script": response.choices[0].message.content.strip(),
        "metadata": {"model": "qwen/qwq-32b:free"},
    }
