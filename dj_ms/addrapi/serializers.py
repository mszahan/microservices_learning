from rest_framework import serializers
from subscription.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'name', 'address', 'postalcode', 'city', 'country', 'email')


