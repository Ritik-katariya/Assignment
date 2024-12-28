import os
from dotenv import load_dotenv

load_dotenv()

TWITTER_USERNAME = os.getenv("TWITTER_USERNAME", "dummy_username")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD", "dummy_password")
PROXYMESH_URL = os.getenv("PROXYMESH_URL", "http://dummy-proxymesh-url")
