from rest_framework import serializers

from .models import PageContent, PageImage, GalleryImage


class PageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageContent
        fields = ['id', 'page_slug', 'section_key', 'title', 'content', 'order']


class PageImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageImage
        fields = ['id', 'page_slug', 'section_key', 'image', 'alt_text', 'caption', 'order']


class GalleryImageSerializer(serializers.ModelSerializer):
    category_display = serializers.CharField(source='get_category_display', read_only=True)

    class Meta:
        model = GalleryImage
        fields = [
            'id', 'category', 'category_display', 'image', 'title',
            'description', 'person_name', 'person_comment', 'year', 'order',
        ]
