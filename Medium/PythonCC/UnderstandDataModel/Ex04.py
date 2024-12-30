# 04. Function and Method Invocation
class CallableObject:
    def __call__(self, *args, **kwargs):
        return f"Called with '{args}'"

obj = CallableObject()
print(obj("Python"))