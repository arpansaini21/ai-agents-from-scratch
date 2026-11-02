from dotenv import load_dotenv
load_dotenv()
import os

print("Hello")
print(os.getenv("openai_api_key"))
print(os.getenv("google_api_key"))
print(os.getenv("ollama_api_key"))
