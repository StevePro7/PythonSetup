# 07. - Multithreading
import threading
import requests

urls = ['http://example.com/file1', 'http://example.com/file2', 'http://example.com/file3']

def download_file(url):
    response = requests.get(url)
    with open(url.split('/')[-1], 'wb') as f:
        f.write(response.content)

threads = []
for url in urls:
    thread = threading.Thread(target=download_file, url=url)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()