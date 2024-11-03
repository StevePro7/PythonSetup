# 04. zip Parallel iteration
names = ['One', 'Two', 'Thr']
score = [85, 90, 95]
for i in range(len(names)):
    print(f"{names[i]} score: {score[i]}")

print()
for name, scre in zip(names, score):
    print(f"{name} score: {scre}")