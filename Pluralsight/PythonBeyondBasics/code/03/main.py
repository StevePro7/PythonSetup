import socket


class Resolver:

    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]

    def clear(self):
        self._cache.clear()


if __name__ == '__main__':
    print('beg')
    resolver = Resolver()
    ip = resolver.__call__('www.google.com')
    print(ip)
    ip2 = resolver.__call__('www.google.com')
    print(ip2)
    print('end')
