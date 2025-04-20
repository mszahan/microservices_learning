from django.urls import path

from .views import AddressList, AddressDetail

ver = 'v1'

urlpatterns = [
    path(f'{ver}/addresses/', AddressList.as_view()),
    path(f'{ver}/addresses/<int:pk>/', AddressDetail.as_view()),
]