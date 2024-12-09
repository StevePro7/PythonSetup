# Error Handling for Secure Data Transmission
import requests

try:
    response = requests.get('https://untrusted-root.badssl.com/', verify=True)
except requests.exceptions.SSLError as e:
    print(f"SSL Error occurred: {e}")