# Typo in variable name
users_list = ["alice", "bob", "charlie"]

# This will now suggest the correct variable name
try:
    print(user_list)  # Intentional typo
except NameError as e:
    print(e)

# Output: name 'user_list' is not defined. Did you mean 'users_list'?