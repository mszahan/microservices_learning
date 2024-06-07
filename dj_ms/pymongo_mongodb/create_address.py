from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import json
from django.core.exceptions import ImproperlyConfigured

with open('secrets.json') as f:
    secrets = json.load(f)


def get_secret(setting, secrets=secrets):
    '''Get the secret variable or return explicit exception.'''
    try:
        return secrets[setting]
    except KeyError:
        error_msg = 'Set the {0} environment variable'.format(setting)
        raise ImproperlyConfigured(error_msg)
    

host = get_secret('DB_HOST')
client = MongoClient(host, server_api=ServerApi('1'))
db = client['Subscription']
col = db['subscription_address']


address = {
    "name": "Monthy Python",
    "address": "Hardwood Lane", 
    "postalcode": "MP1", "city": 
    "London", "country": "England", 
    "email": "monthy@python.com" 
           }

col.insert_one(address)