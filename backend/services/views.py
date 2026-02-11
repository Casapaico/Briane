from rest_framework import generics

from .models import Service
from .serializers import ServiceSerializer


class ServiceListView(generics.ListAPIView):
    serializer_class = ServiceSerializer
    pagination_class = None
    queryset = Service.objects.filter(is_active=True)


class ServiceDetailView(generics.RetrieveAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.filter(is_active=True)
    lookup_field = 'slug'
