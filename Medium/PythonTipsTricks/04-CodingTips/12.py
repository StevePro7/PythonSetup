# 12. Using defaultdict: simplify dictionary operations
word_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
word_count = {}

for word in word_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)
print()

# Condensed way: using defaultdict
from collections import defaultdict
word_count2 = defaultdict(int)

for word in word_list:
    word_count2[word] += 1

print(word_count2)