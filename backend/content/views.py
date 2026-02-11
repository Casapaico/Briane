from rest_framework import generics

from .models import PageContent, PageImage, GalleryImage
from .serializers import PageContentSerializer, PageImageSerializer, GalleryImageSerializer


class PageContentListView(generics.ListAPIView):
    serializer_class = PageContentSerializer
    pagination_class = None

    def get_queryset(self):
        slug = self.kwargs['slug']
        return PageContent.objects.filter(page_slug=slug, is_active=True)


class PageImageListView(generics.ListAPIView):
    serializer_class = PageImageSerializer
    pagination_class = None

    def get_queryset(self):
        slug = self.kwargs['slug']
        return PageImage.objects.filter(page_slug=slug, is_active=True)


class GalleryImageListView(generics.ListAPIView):
    serializer_class = GalleryImageSerializer
    pagination_class = None

    def get_queryset(self):
        category = self.kwargs['category']
        return GalleryImage.objects.filter(category=category, is_active=True)
