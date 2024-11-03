# 14. f-strings: simplify string formatting
name = "Alice"
age = 30
greeting = "Hello, my name is {} and I am {} years old.".format(name, age)
print(greeting)
print()

# Condensed way: using f-strings
name = "Alice"
age = 30
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)