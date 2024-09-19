import time

print('beg')

def say_hello():
    time.sleep(2)
    print("Hello async world")

say_hello()
print('end')