from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CompanyInfo, Stat, TeamMember, Client, NewsArticle
from .serializers import (
    CompanyInfoSerializer, StatSerializer, TeamMemberSerializer,
    ClientSerializer, NewsArticleSerializer, NewsArticleListSerializer,
)


class CompanyInfoView(APIView):
    def get(self, request):
        info = CompanyInfo.load()
        serializer = CompanyInfoSerializer(info, context={'request': request})
        return Response(serializer.data)


class StatListView(generics.ListAPIView):
    serializer_class = StatSerializer
    pagination_class = None
    queryset = Stat.objects.filter(is_active=True)


class TeamMemberListView(generics.ListAPIView):
    serializer_class = TeamMemberSerializer
    pagination_class = None
    queryset = TeamMember.objects.filter(is_active=True)


class ClientListView(generics.ListAPIView):
    serializer_class = ClientSerializer
    pagination_class = None
    queryset = Client.objects.filter(is_active=True)


class NewsArticleListView(generics.ListAPIView):
    serializer_class = NewsArticleListSerializer
    queryset = NewsArticle.objects.filter(is_published=True)


class NewsArticleDetailView(generics.RetrieveAPIView):
    serializer_class = NewsArticleSerializer
    queryset = NewsArticle.objects.filter(is_published=True)
    lookup_field = 'slug'
