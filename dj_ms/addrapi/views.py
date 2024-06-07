from rest_framework.views import APIView
from rest_framework.response import Response
from subscription.models import Address
from .serializers import AddressSerializer



class AddressList(APIView):
    def get(self, request, format=None):
        addresses = Address.objects.all()
        serializer = AddressSerializer(addresses, many=True)
        return Response(serializer.data)
