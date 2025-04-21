import datetime
from celery import Celery
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import json
from django.core.exceptions import ImproperlyConfigured

with open('../secrets.json') as f:
    secrets = json.load(f)


def get_secret(setting, secrets=secrets):
    '''Get the secret variable or return explicit exception.'''
    try:
        return secrets[setting]
    except KeyError:
        error_msg = 'Set the {0} environment variable'.format(setting)
        raise ImproperlyConfigured(error_msg)

## main codee......................................................

#sets rabbitmq as the broker
app = Celery('log', broker ='pyamqp://guest@localhost//')


@app.task()
def write_logitem(application, logmessage):
    now = datetime.datetime.now()
    uri = get_secret('DB_HOST')
    client = MongoClient(uri, server_api=ServerApi('1'))
    subscription_db = client['Subscription']
    logitem_col = subscription_db["subscription_logitem"]

    logitem_col.insert_one({'time': now.strftime("%Y-%m-%d %H:%M:%S"),
                            'app': application,
                            'logmessage': logmessage})
    print(f'[{now.strftime("%Y-%m-%d %H:%M:%S")}] - new logmessage entered')