import json
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='mail_queue', durable=True)


def callback(ch, method, properties, body):
    mail_message = json.loads(body)
    print(f'Email sent to {mail_message["name"]} at {mail_message["email"]} with subject "{mail_message["subject"]}"')

channel.basic_consume(
    queue='mail_queue',
    on_message_callback=callback,
    auto_ack=True
)

channel.start_consuming()