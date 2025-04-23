import requests
from celery import shared_task
from django.core.mail import send_mail
from rapidfuzz import fuzz
from .models import Address





@shared_task
def match_address_task(address):
    respose = requests.get('http://localhost:8000/api/v1/addresses/')
    addresses = [a_address['address'] for a_address in respose.json()]

    top_score = 0
    min_score = 70
    match_address = address['address']
    for base_address in addresses:
        score = round(fuzz.ratio(address['address'].lower(), str(base_address).lower()))
        if score >= top_score and score >= min_score:
            top_score = score
            match_address = base_address
        if top_score == 100:
            break
    print(f'Match address: {match_address} > Score : {top_score}')
    address = {'name': address['name'],
               'address': match_address,
               'postalcode': address['postalcode'],
               'city': address['city'],
               'country': address['country'],
               'email': address['email']}
    response = requests.post('http://localhost:8000/api/v1/addresses/', data=address)
    print(f'New address inserted for {address["name"]}')
    send_email_task.delay(address['name'], address['email'])



@shared_task
def send_email_task(name, email):
    send_mail(
        'Subscription Confirmation',
        f'Thank you for subscribing, {name}!',
        'magazine@cm-publisher.com',
        [email],
        fail_silently=False,)

