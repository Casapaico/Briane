from rest_framework import serializers

from .models import CompanyInfo, Stat, TeamMember, Client, NewsArticle


class CompanyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyInfo
        fields = [
            'name', 'tagline', 'description', 'mission', 'vision', 'values',
            'address', 'phones', 'emails', 'hours', 'social_links',
            'google_maps_embed_url', 'whatsapp_number',
        ]


class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = ['id', 'value', 'label', 'suffix', 'order']


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ['id', 'name', 'position', 'bio', 'image', 'order']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'logo', 'url', 'order']


class NewsArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArticle
        fields = ['id', 'title', 'slug', 'excerpt', 'content', 'date', 'category', 'image']


class NewsArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArticle
        fields = ['id', 'title', 'slug', 'excerpt', 'date', 'category', 'image']
