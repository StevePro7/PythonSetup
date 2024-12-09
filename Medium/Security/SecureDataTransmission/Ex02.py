# 2. Verify SSL/TLS Certificates
import requests

try:
    # This will raise exception if certificate not valid
    response = requests.get('https://google.com', verify=True)
    print(response.content)
except requests.exceptions.SSLError as e:
    print(f"SSL verification failed {e}")