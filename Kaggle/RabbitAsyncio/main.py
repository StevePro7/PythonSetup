import pika
import json
import asyncio


async def thread01(channel, file01_path, message01_byte):
    channel.basic_publish(exchange='', routing_key='trigger', body=message01_byte)
    print(f" [x] Sent Thread #01 '{file01_path}")


async def thread02(channel, file02_path, message02_byte):
    channel.basic_publish(exchange='', routing_key='trigger_rule', body=message02_byte)
    print(f" [x] Sent Thread #02 '{file02_path}")


async def main():
    # Define connectio parameters
    credentials = pika.PlainCredentials('<redacted>', '<redacted>')
    parameters = pika.ConnectionParameters(
        host='localhost',
        port=5672,
        credentials=credentials
    )

    # Establish connection and channel
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    # Publish a message to the 'trigger' queue
    file01_path = "file01.json"
    file02_path = "file02.json"
    with open(file01_path, 'r') as file01:
        message01_dict = json.load(file01)

    with open(file02_path, 'r') as file02:
        message02_dict = json.load(file02)

    message01_json = json.dumps(message01_dict)
    message01_byte = message01_json.encode('utf-8')

    message02_json = json.dumps(message02_dict)
    message02_byte = message02_json.encode('utf-8')

    tasks = []
    for _ in range(4096):
        tasks.append(thread01(channel, file01_path, message01_byte))
        tasks.append(thread02(channel, file02_path, message02_byte))
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
