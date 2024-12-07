# 4. Thread Communication
import threading
import random
from queue import Queue

def producer(queue):
    print('Producer: running')
    for i in range(10):
        value = random.random()
    queue.put(None)
    print('Producer: done')

def consumer(queue):
    print('Consumer: running')
    while True:
        item = queue.get()
        if item is None:
            break
        print(f'>got {item}')
    print('Consumer: done')

queue = Queue()
consumer = threading.Thread(target=consumer, args=(queue,))
consumer.start()

producer = threading.Thread(target=producer, args=(queue,))
producer.start()

producer.join()
consumer.join()