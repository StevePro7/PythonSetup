from tqdm import tqdm
import time


for i in tqdm(range(100), desc="Processing", mininterval=0.5):
    time.sleep(0.1)
