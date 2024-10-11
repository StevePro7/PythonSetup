for tqdm import tqdm


paths = os.walk('/')

for fpath in tqdm(paths, desc="Looping over root dir"):
	...
	