from django.urls import path
from .views import NewsItemApiView

urlpatterns = [
    path('', NewsItemApiView.as_view() )
]