import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

SPLUNK_HEC_TOKEN=os.getenv("SPLUNK_HEC_TOKEN")
SPLUNK_HEC_ENDPOINT = 'https://localhost:8088/services/collector/event'

headers = {
    'Authorization': f'Splunk {SPLUNK_HEC_TOKEN}',
    'Content-Type': 'application/json'
}
log_event = {
    "event": {
        "level": "info",
        "message": "This is a test log from Steven...utils",
        "user": "stevepro"
    },
    "sourcetype": "steven-python",
    "host": "localhost",
    "index": "main"
}

data=json.dumps(log_event)
response = requests.post(SPLUNK_HEC_ENDPOINT, headers=headers, data=data, verify=False)
#response = requests.post(SPLUNK_HEC_ENDPOINT, headers=headers, json=data, verify=False)
response.raise_for_status()
print(response.status_code, response.text)
print('the end')