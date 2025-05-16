import logging
import threading
import queue
import time

log_queue = queue.Queue()

def log_worker():
    while True:
        record = log_queue.get()
        # Sentinel to shut down the thread
        if record is None:
            break
        logger = logging.getLogger(record.name)
        logger.handle(record)

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(message)s")

def thread_task(thread_id):
    thread_name = f"Thread-{thread_id}"
    record = logging.LogRecord(thread_name, logging.INFO, "", 0, f"{thread_name} is working", None, None)
    log_queue.put(record)

log_thread = threading.Thread(target=log_worker, daemon=True)
log_thread.start()

threads = []
for i in range(2):
    thread = threading.Thread(target=thread_task, args=(i,))
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

# Stop the logging thread
log_queue.put(None)
log_thread.join()