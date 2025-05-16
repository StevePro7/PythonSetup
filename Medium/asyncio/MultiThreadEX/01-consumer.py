import pika
import time
from concurrent.futures import ThreadPoolExecutor

def callback(ch, method, properties, body):
    """
    Callback function to handle messages from the queue
    """
    print(f"Received message: {body.decode()}")
    # Simulate I/O bound work (e.g., interacting with a database)
    time.sleep(2)  # Simulate a blocking I/O operation like a DB query
    print(f"Processed message: {body.decode()}")

def consume():
    """
    Connect to RabbitMQ, declare a queue, and start consuming messages
    """
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    
    channel.queue_declare(queue='my_queue')
    
    print('Waiting for messages. To exit press CTRL+C')
    channel.basic_consume(queue='my_queue', on_message_callback=callback, auto_ack=True)
    
    # Start consuming messages in the background
    channel.start_consuming()

def main():
    """
    Start multiple threads to consume messages concurrently
    """
    with ThreadPoolExecutor(max_workers=5) as executor:
        for _ in range(5):
            executor.submit(consume)  # Start multiple consumers in parallel

if __name__ == '__main__':
    main()
