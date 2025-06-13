import dis
def greet(name: str) -> None:
    return f"Hello, {name}"

#g=greet("stevepro")
#print(g)

print(dis.dis(greet))
