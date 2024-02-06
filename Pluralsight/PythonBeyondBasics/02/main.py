import reader

r = reader.Reader("foo.txt")

try:
    res = r.read()
    print(res)
finally:
    r.close()
