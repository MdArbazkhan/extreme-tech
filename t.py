import os

# for env variable
from dotenv import load_dotenv
load_dotenv()

api_key = os.environ.get("mailjet_api_key")
api_secret = os.environ.get("mailjet_api_secret")

print(api_key, api_secret)