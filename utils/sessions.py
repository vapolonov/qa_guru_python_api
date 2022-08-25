import os
from utils.requests_helper import BaseSession
from dotenv import load_dotenv


def cats() -> BaseSession:
    load_dotenv()
    cats_url = os.getenv('cats_api')
    return BaseSession(base_url=cats_url)
