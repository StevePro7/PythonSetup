def count_up_to(n):
    num = 0
    while num < n:
        yield num
        num += 1

for i in count_up_to(3):
    print(i)