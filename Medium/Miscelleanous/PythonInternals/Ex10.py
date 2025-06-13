class MyCustomError(Exception):
    pass

def risky():
    raise MyCustomError("Something went wrong")


try:
    risky()
except MyCustomError as e:
    print(e)