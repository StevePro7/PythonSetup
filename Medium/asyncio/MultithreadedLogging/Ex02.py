import logging
import threading

def create_logger(thread_name):
    logger = logging.getLogger(thread_name)
    if not logger.hasHandlers():
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        file_handler = logging.FileHandler(f"logEx02-{thread_name}.log")
        file_handler.setFormatter(formatter)

        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)
    return logger

def thread_task(thread_id):
    thread_name = f"Thread-{thread_id}"
    logger = create_logger(thread_name)
    logger.info(f"Starting task in {thread_name}")
    logger.info(f"EndingTO task in {thread_name}")

logger_main = create_logger("Main")
logger_main.info("Startup")

threads = []
for i in range(2):
    thread = threading.Thread(target=thread_task, args=(i,))
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

logger_main.info("Teardown")