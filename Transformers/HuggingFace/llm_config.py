import os
from dotenv import load_dotenv

load_dotenv()

repo_id = "mistralai/Mistral-7B-Instruct-v0.3" #calling this model as an API
api_key = os.getenv("HF_TOKEN")