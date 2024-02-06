import os

from reader.compressed import bzipped

extension_map = {
    '.bz2': bzipped.opener,
}

class Reader:
    def __init__(self, filename):
        extension = os.path.splitext(filename)[1]
        print(f"hi: '{extension}'")
        opener = extension_map.get(extension, open)
        self.f = opener(filename, 'rt')
        print(self.f)

    def foo(self):
        print('foo')