from django.urls import path

from .views import AddressList

ver = 'v1'

urlpatterns = [
    path(f'{ver}/addresses', AddressList.as_view())
]