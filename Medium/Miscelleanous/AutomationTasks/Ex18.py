# 18. Automate Task Scheduling
import schedule
import time


def task():
    print("Task running!")


schedule.every().day.at("10:00").do(task)


while True:
    schedule.run_pending()
    time.sleep(1)
