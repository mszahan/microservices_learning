from django.urls import path, include
from rest_framework.routers import DefaultRouter

# from .views import AddressList, AddressDetail
from .views import AddressViewSet

ver = 'v1'

router = DefaultRouter()
router.register(f'{ver}/addresses', AddressViewSet, basename='address')

urlpatterns = [
    # path(f'{ver}/addresses/', AddressList.as_view()),
    # path(f'{ver}/addresses/<int:pk>/', AddressDetail.as_view()),
    path('', include(router.urls)),
]