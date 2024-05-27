from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import NewsItemSerializer
from .models import NewsItem



class NewsItemApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @method_decorator(cache_page(15 *60))
    def get(self, request, *args, **kwargs):
        new_items = NewsItem.objects.all().order_by('time_stamp')
        serializer = NewsItemSerializer(new_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


