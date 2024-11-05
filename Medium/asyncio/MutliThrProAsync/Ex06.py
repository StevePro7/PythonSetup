# 06. - Multiprocessing
import multiprocessing as mp

def process_data(data_chunk):
    # Perform some data processing here
    return sum(data_chunk)

if __name__ == '__main__':
    data = [range(1000000), range(1000000, 2000000), range(2000000, 3000000)]
    with mp.Pool(processes=3) as pool:
        results = pool.map(process_data, data)
        print(results)