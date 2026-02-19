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
        serializer = CompanyInfoSerializer(info)
        return Response(serializer.data)


class StatListView(generics.ListAPIView):
    serializer_class = StatSerializer
    queryset = Stat.objects.filter(is_active=True)
    pagination_class = None


class TeamMemberListView(generics.ListAPIView):
    serializer_class = TeamMemberSerializer
    queryset = TeamMember.objects.filter(is_active=True)
    pagination_class = None


class ClientListView(generics.ListAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.filter(is_active=True)
    pagination_class = None


class NewsArticleListView(generics.ListAPIView):
    serializer_class = NewsArticleListSerializer
    queryset = NewsArticle.objects.filter(is_published=True)


class NewsArticleDetailView(generics.RetrieveAPIView):
    serializer_class = NewsArticleSerializer
    queryset = NewsArticle.objects.filter(is_published=True)
    lookup_field = 'slug'
