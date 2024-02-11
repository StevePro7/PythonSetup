def median(iterable):
    if len(iterable) == 0:
        raise ValueError("median() arg is an empty sequence")

    items = sorted(iterable)
    median_index = (len(items) - 1) // 2
    if len(items) % 2 != 0:
        return items[median_index]

    return (items[median_index] + items[median_index + 1]) / 2.0


def main():
    try:
        median([])
    except ValueError as e:
        print("Payload: ", e.args)


if __name__ == '__main__':
    main()
