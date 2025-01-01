# 10. File Handling
# Read File
with open("data.txt", "r") as file:
    content = file.read()

# Write File
with open("output.txt", "w") as file:
    file.write("Hello, World!")