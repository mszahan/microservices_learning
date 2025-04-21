import json
import pika

connnection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connnection.channel()
channel.queue_declare(queue='mail_queue', durable=True)

for idx in range(1, 6):
    mail_task = {
        'name': f'M. MCDoe{idx}',
        'email':f'mcdoe{idx}@xyz.com',
        'subject': f'Hello M. MCDoe{idx}',
        'body': f'Hello M. MCDoe{idx},\n\nThis is a test email.\n\nBest regards,\nYour Company'
    }
    channel.basic_publish(
        exchange='',
        routing_key='mail_queue',
        body=json.dumps(mail_task),
        properties=pika.BasicProperties(
            delivery_mode=pika.DeliveryMode.Persistent
        )
    )

connnection.close()