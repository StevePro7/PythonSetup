letters = ["a", "b", "c"]
numbers = [1, 2]

for letter in letters:
	for number in numbers:
		print(f"{letter}{number}")
		

combined_items = [l + str(n) for l in letters for n in numbers]
print(combined_items)
