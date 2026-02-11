from rest_framework import generics

from .models import NewsArticle
from .serializers import NewsArticleSerializer, NewsArticleListSerializer


class NewsArticleListView(generics.ListAPIView):
    serializer_class = NewsArticleListSerializer
    queryset = NewsArticle.objects.filter(is_published=True)


class NewsArticleDetailView(generics.RetrieveAPIView):
    serializer_class = NewsArticleSerializer
    queryset = NewsArticle.objects.filter(is_published=True)
    lookup_field = 'slug'
