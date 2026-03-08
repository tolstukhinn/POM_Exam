import os
from dotenv import load_dotenv
load_dotenv()


class UserData:
    FIRST_NAME = os.getenv("FIRST_NAME")
    LAST_NAME = os.getenv("LAST_NAME")
    ZIP_CODE = os.getenv("ZIP_CODE")