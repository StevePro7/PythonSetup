def read_time_by_line(filename: str) -> str:
    for row in open(filename, 'r'):
        yield row


# IMPORTANT
# type(x) = <class generator>
x = read_time_by_line('README.md')
print(x)
for i in x:
    print(i)
#for line in read_time_by_line('README.md'):
#    print(line)
