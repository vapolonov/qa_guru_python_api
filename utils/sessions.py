import os
from utils.requests_helper import BaseSession
from dotenv import load_dotenv


def cats() -> BaseSession:
    load_dotenv()
    cats_url = os.getenv('cats_api')
    return BaseSession(base_url=cats_url)


def reqres() -> BaseSession:
    load_dotenv()
    reqres_url = os.getenv('reqres_api')
    return BaseSession(base_url=reqres_url)