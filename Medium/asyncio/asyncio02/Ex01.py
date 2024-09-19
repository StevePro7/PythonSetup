async def coroutine_multiply_by_two(number: int) -> int:
    return number * 2

def multiply_by_two(number: int) -> int:
    return number * 2

function_result = multiply_by_two(2)
coroutine_result = coroutine_multiply_by_two(2)

print(f'Function result is {function_result} and the type is {type(function_result)}')
print(f'Coroutine result is {coroutine_result} and the type is {type(coroutine_result)}')
