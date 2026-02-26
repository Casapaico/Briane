from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import GalleryImage, PageContent
from .serializers import GalleryImageSerializer, PageContentSerializer


class GalleryImageListView(generics.ListAPIView):
    serializer_class = GalleryImageSerializer
    pagination_class = None

    def get_queryset(self):
        category = self.kwargs['category']
        return GalleryImage.objects.filter(category=category, is_active=True)


class PageContentDetailView(APIView):
    def get(self, request, page_slug, section_key):
        try:
            obj = PageContent.objects.get(page_slug=page_slug, section_key=section_key, is_active=True)
            return Response(PageContentSerializer(obj).data)
        except PageContent.DoesNotExist:
            return Response({}, status=404)
