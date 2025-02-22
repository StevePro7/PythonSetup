import re
from tqdm import tqdm
from multiprocessing import Pool


def calc_num_matches(string):
    # We create a separate function for our Pool object
    # It will be applied in parallel to every line in the file
    pattern = r"[0-9]{1}[rb]ob"
    return len(re.findall(pattern, string))


def chunks_single_pool():
    num_total_matches = 0

    pool = Pool(8)  # number of processes, should be <= number of your CPU cores

    with open('random.txt', 'rt') as f:
        chunk = []
        # We load lines in a list 
        for line in tqdm(f, total=1_000_000):
            line = line.lower()
            chunk.append(line)

            if len(chunk) == 1000:
                # And then we apply our `calc_num_matches` function to every line in parallel
                num_ind_matches = pool.map(calc_num_matches, chunk)
                # And add together all the independent matches
                num_matches = sum(num_ind_matches)
                num_total_matches += num_matches

                chunk = []

    return num_total_matches


chunks_single_pool()
