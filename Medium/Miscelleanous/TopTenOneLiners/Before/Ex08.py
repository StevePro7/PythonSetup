# 8. Find All Indices of a Substring in a String
def find_all(text, substring):
    indices = []
    index = -1
    while True:
        index = text.find(substring, index + 1)
        if index == -1:
            return indices
        indices.append(index)


result = find_all("StevePro Studios", "eve")
print(result)
