import json
import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
# exchange declaration makes it publish/subscribe
channel.exchange_declare(exchange='email', exchange_type='fanout')

for idx in range(1,6):
    mail_task = {
        'name': f'M. MCDoe{idx}',
        'email': f'mcdoe{idx}@xyz.com',
        'subject': f'Hello MCDoe{idx}',
        'body': f'Hello MCDoe{idx}, this is a test email.'
    }
    # publish the message to the exchange
    channel.basic_publish(
        exchange='email',
        routing_key='',
        body=json.dumps(mail_task)
    )


connection.close()