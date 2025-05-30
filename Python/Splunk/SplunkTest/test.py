import os
from dotenv import load_dotenv

load_dotenv()
SPLUNK_HEC_TOKEN=os.getenv("SPLUNK_HEC_TOKEN")
print(f"token='{SPLUNK_HEC_TOKEN}'")