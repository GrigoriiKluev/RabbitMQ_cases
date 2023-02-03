import pika
import time
import random

from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

#channel.queue_declare(queue='letterbox')
channel.exchange_declare(exchange='mytopicexchange', exchange_type=ExchangeType.topic)

user_payments_message  = 'A european user paid for something'

channel.basic_publish(exchange='mytopicexchange', routing_key='user.europe.payments', body=user_payments_message)

print(f'sent message {user_payments_message}')

business_order_message = 'A european business ordered goods'

channel.basic_publish(exchange='mytopicexchange', routing_key='business.europe.order', body=business_order_message)

print(f'sent message {business_order_message}')

connection.close()
