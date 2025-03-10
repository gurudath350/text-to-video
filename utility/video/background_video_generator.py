import os
import requests
from dotenv import load_dotenv

load_dotenv()

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")

def generate_video_url(
    search_queries: List[Tuple[float, float, List[str]]]
) -> List[Tuple[float, float, str]]:
    headers = {"Authorization": PEXELS_API_KEY}
    video_urls = []
    
    for start, end, queries in search_queries:
        for query in queries:
            response = requests.get(
                "https://api.pexels.com/videos/search",
                headers=headers,
                params={"query": query, "per_page": 1},
            )
            if response.status_code == 200:
                videos = response.json()["videos"]
                if videos:
                    video_url = videos[0]["video_files"][0]["link"]
                    video_urls.append((start, end, video_url))
                    break
        else:
            video_urls.append((start, end, "fallback_video.mp4"))
    
    return video_urls
