# Traditional approach - immediate evaluation
name = "Alice"
greeting = f"Hello, {name}!"  # Evaluates immediately
print(greeting)  # Hello, Alice!

# New t-string approach - deferred evaluation
template = t"Hello, {name}!"  # Creates a template, doesn't evaluate yet

# Now we can reuse this template with different contexts
context1 = {"name": "Bob"}
context2 = {"name": "Charlie"}

print(template.substitute(context1))  # Hello, Bob!
print(template.substitute(context2))  # Hello, Charlie!