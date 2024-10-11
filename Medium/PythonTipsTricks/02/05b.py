import functools

@functools.singledispatch
def process_data(address):
    raise TypeError('Wrong address format!')
	
@process_data.register
def _(address: str):
    ip, port = address.split(':')
    print(f'IP：{ip}, Port：{port}')
	
@process_data.register
def _(address: tuple):
    ip, port = address
    print(f'IP：{ip}, Port：{port}')

process_data('johni.medium.com:443')     # johni.medium.com, Port：443
process_data(('johni.medium.com', 443))  # johni.medium.com, Port：443
process_data(2077)                       # TypeError: Wrong address format!