from rest_framework import serializers

from .models import GalleryImage, PageContent


class GalleryImageSerializer(serializers.ModelSerializer):
    category_display = serializers.CharField(source='get_category_display', read_only=True)

    class Meta:
        model = GalleryImage
        fields = [
            'id', 'category', 'category_display', 'image', 'title',
            'description', 'person_name', 'person_comment', 'year', 'order',
        ]


class PageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageContent
        fields = ['id', 'page_slug', 'section_key', 'title', 'content']
