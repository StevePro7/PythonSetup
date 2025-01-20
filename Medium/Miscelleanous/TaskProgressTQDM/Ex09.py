import requests
from tqdm import tqdm

url = "https://example.com/largefile.zip"
response = requests.get(url, stream=True)

total_size = int(response.headers.get('content-length', 0))
block_size = 1024  # 1 Kibibyte

with open("largefile.zip", "wb") as file, tqdm(
    desc="Downloading",
    total=total_size,
    unit='iB',
    unit_scale=True,
    unit_divisor=1024,
) as bar:
    for data in response.iter_content(block_size):
        bar.update(len(data))
        file.write(data)