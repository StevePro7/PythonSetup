# Weird - cannot see the following attributes

def main():
    try:
        u = b'\x81'.decode('utf-8')
        print(u)
    except UnicodeDecodeError as e:
        print(e)
        print("encoding:", e.encoding)
        print("reason:", e.reason)
        print("object:", e.object)
        print("start:", e.start)
        print("end:", e.end)


if __name__ == '__main__':
    main()
