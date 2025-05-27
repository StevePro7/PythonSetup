import pika
import json
import asyncio


async def thread01(channel, file01_path, message01_byte):
    channel.basic_publish(exchange='', routing_key='trigger', body=message01_byte)
    print(f" [x] Sent Thread #01 '{file01_path}")


async def thread02(channel, file02_path, message02_byte):
    channel.basic_publish(exchange='', routing_key='trigger_rule', body=message02_byte)
    print(f" [x] Sent Thread #02 '{file02_path}")


async def load_file(file_path) -> bytes:
    with open(file_path, 'r') as file:
        message_dict = json.load(file)

    message_json = json.dumps(message_dict)
    return message_json.encode('utf-8')


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
    message01_byte = await load_file(file01_path)

    file02_path = "file02.json"
    message02_byte = await load_file(file02_path)

    tasks = []
    for _ in range(4096):
        tasks.append(thread01(channel, file01_path, message01_byte))
        tasks.append(thread02(channel, file02_path, message02_byte))
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
