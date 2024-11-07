# 10. - Multiprocessing
import multiprocessing as mp

def worker(queue):
    queue.put("Hello from a worker!")

if __name__ == '__main__':
    queue = mp.Queue()
    process = mp.Process(target=worker, args=(queue,))
    process.start()
    process.join()
    print(queue.get())  # Output: Hello from a worker!