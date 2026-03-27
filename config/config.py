import os

class Config:
    BASE_URL = os.getenv("BASE_URL", "http://www.example.com")
    BROWSER = os.getenv("BROWSER", "chrome")
    HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"
    IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "10"))
    EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "20"))
    SCREENSHOT_PATH = os.getenv("SCREENSHOT_PATH", "screenshots")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    API_BASE_URL = os.getenv("API_BASE_URL", "http://jsonplaceholder.typicode.com")
