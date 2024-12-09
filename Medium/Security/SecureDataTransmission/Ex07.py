# 7. Manage Configuration Securely
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

api_key = os.getenv('API_KEY')
print(f"API Key: {api_key}")