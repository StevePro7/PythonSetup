from tqdm import tqdm
import time


for i in tqdm(range(100), desc="Processing", ncols=75):
    time.sleep(0.1)
