# 8. Find All Indices of a Substring in a String
text = "StevePro Studios"
substring = "eve"
indices = [i for i in range(len(text)) if text.startswith(substring, i)]

print(indices)
