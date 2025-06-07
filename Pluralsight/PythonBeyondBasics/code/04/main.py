#tracer
class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)
        return wrap


tracer = Trace()

@tracer
def rotate_list(l):
    return l[1:] + [l[0]]


if __name__ == '__main__':
    print('beg')
    l = [1,2,3]
    print(l)
    m = rotate_list(l)
    print(m)
    print('end')
