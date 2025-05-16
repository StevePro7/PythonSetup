import logging
import threading

class RequestHandler:
    def __init__(self, user_id):
        self.user_id = user_id
        self.logger = logging.getLogger(f"User-{user_id}")
        if not self.logger.hasHandlers():
            self.logger.setLevel(logging.DEBUG)
            handler = logging.FileHandler(f"logEx03-user_{user_id}.log")
            handler.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
            self.logger.addHandler(handler)

    def process_request(self):
        self.logger.info(f"Processing request for user {self.user_id}")
        self.logger.info(f"Completing request for user {self.user_id}")

def simulate_user_request(user_id):
    handler = RequestHandler(user_id)
    handler.process_request()

threads = []
for user_id in range(2):
    thread = threading.Thread(target=simulate_user_request, args=(user_id,))
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
