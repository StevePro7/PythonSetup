class MyContextManager:
	def __enter__(self):
		resource = object()
		return resource
		
	def __exit__(self, exe_type, exe_value, traceback):
		...
		
# using the context manager
with MyContextManager() as ctx:
	print(ctx)
		
		
@contextmanager
def my_context_manager():
	resource = object()
	try:
		yield resource
	finally:
		# clean up the resource
		...
		
		
with my_context_manager() as ctx:
	print(ctx)