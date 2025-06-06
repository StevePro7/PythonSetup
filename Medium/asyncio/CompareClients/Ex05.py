import time
import requests

url = 'https://www.leapcell.io'
headers = {
    'User-Agent'
    '': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}

def make_request():
    response = requests.get(url, headers=headers)
    print(response.status_code)

def main():
    num: int = 10
    start = time.time()
    for _ in range(num):
        make_request()
    end = time.time()
    print(f'sent {num} requests, cost: {end - start}')

if __name__ == '__main__':
    main()