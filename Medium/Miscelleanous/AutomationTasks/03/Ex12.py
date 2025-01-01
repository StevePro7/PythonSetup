# 12. Automate Website Monitoring
import requests
import time


def monitor_website(url, interval):
    prev_content = None
    while True:
        response = requests.get(url)
        if response.text != prev_content:
            print("Website updated!")
            prev_content = response.text
        time.sleep(interval)
