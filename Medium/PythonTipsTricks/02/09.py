while (value := input('Type something: ')) != 'exit':
	print(value)
	
	
entries = [
	{
		"name": "Lisa",
	},
	{
		"name": "",
	},
]

for entry in entries:
	if name := entry.get("name"):
		print(f'Found name: "{name}"')
		
		
numbers = [1,2,4,5,6,6,89]
if (length := len(numbers)) >= 5:
	print("The length of the list is: ", length)
	