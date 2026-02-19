from rest_framework import generics

from .models import Service
from .serializers import ServiceSerializer, ServiceListSerializer


class ServiceListView(generics.ListAPIView):
    serializer_class = ServiceListSerializer
    queryset = Service.objects.filter(is_active=True)
    pagination_class = None


class ServiceDetailView(generics.RetrieveAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.filter(is_active=True)
    lookup_field = 'slug'
