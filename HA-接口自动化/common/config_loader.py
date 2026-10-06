import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

class Config:
    def __init__(self):
        self.base_url = os.getenv("HA_BASE_URL", "http://192.168.222.128:8123").rstrip("/")
        self.token = os.getenv("HA_TOKEN", "")
        self.timeout = int(os.getenv("HA_TIMEOUT", "10"))

config = Config()
