from rest_framework import generics

from .models import GalleryImage
from .serializers import GalleryImageSerializer


class GalleryImageListView(generics.ListAPIView):
    serializer_class = GalleryImageSerializer
    pagination_class = None

    def get_queryset(self):
        category = self.kwargs['category']
        return GalleryImage.objects.filter(category=category, is_active=True)
