from tqdm import tqdm
import time


def process_item(item):
    time.sleep(0.1)


items = range(100)
for item in tqdm(items, desc="Processing"):
    process_item(item)
