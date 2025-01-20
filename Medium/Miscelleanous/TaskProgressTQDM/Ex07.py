from tqdm import tqdm
import time

for i in tqdm(range(10), desc="Outer Loop"):
    for i in tqdm(range(100), desc="Innter Loop", leave=False):
        time.sleep(0.1)