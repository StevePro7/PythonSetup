import functools

@functools.singledispatch
def process_data(data):
	print("Generic processing: ", data)
	
@process_data.register(int)
def _(data):
	print("Processing integer data: ", data)
	
@process_data.register(list)
def _(data):
	print("Processing list data: ", data)
	
process_data("Hello")    # Generic processing: Hello
process_data(42)         # Processing integer data: 42
process_data([1, 2, 3])  # Processing list data: [1, 2, 3]