import multiprocessing

def count():
    for i in range(1000000):
        pass


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=count)
    p2 = multiprocessing.Process(target=count)
    p1.start()
    p2.start()
    p1.join()
    p2.join()


# import threading
#
# def count():
#     for i in range(1000000):
#         pass
#
#
# if __name__ == "__main__":
#     t1 = threading.Thread(target=count)
#     t2 = threading.Thread(target=count)
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()