import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare("simplehashing", "x-consistent-hash")

routing_key = "Hash me"

message = " This is the Core message"

channel.basic_publish(
    exchange='simplehashing',
    routing_key=routing_key,
    body=message)

print(f"sent message: {message}")

connection.close()