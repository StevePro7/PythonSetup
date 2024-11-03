# 06. collections: Powerful data structures
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)

print()
# Condensed way using counter
from collections import Counter
word_count2 = Counter(words)
print(word_count2)
print(word_count['apple'])
