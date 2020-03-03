import os
from dotenv import load_dotenv


class Setting:
    def __init__(self):
        load_dotenv()
        self.debug = os.getenv("DEBUG")
        self.origin_url = os.getenv("ORIGIN_URL")
        self.referer_url = os.getenv("REFERER_URL")
        self.api_url = os.getenv("API_URL")
        self.sleep = int(os.getenv("SLEEP") or 0)
