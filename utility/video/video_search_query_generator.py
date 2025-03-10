from typing import List, Tuple
import re

def get_video_search_queries_timed(
    script: str, timed_captions: List[Tuple[float, float, str]]
) -> List[Tuple[float, float, List[str]]]:
    keywords = re.findall(r"\b\w+\b", script.lower())
    search_queries = []
    
    for start, end, text in timed_captions:
        query = " ".join([word for word in keywords if word in text.lower()][:3])
        search_queries.append((start, end, [query]))
    
    return search_queries
