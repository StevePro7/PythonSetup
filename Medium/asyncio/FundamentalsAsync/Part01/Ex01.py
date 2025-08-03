import time


def fetch_data(source):
    """
    """
    print(f"BEG {source}")
    time.sleep(2)
    print(f"end {source}")


def main():
    start = time.time()

    result1 = fetch_data("API #1")
    result2 = fetch_data("API #2")
    result3 = fetch_data("API #3")

    print(f"Total: {time.time()-start:.2f}")


if __name__ == '__main__':
    main()
