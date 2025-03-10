import logging

def setup_logging():
    logging.basicConfig(
        filename="video_generation.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
