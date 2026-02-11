from django.contrib import admin
from django.utils.html import format_html

from .models import NewsArticle


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'category', 'image_preview', 'is_published']
    list_filter = ['is_published', 'category', 'date']
    search_fields = ['title', 'excerpt', 'content']
    list_editable = ['is_published']
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = [
        ('Contenido', {'fields': ['title', 'slug', 'excerpt', 'content']}),
        ('Clasificacion', {'fields': ['date', 'category']}),
        ('Imagen', {'fields': ['image']}),
        ('Publicacion', {'fields': ['is_published']}),
    ]

    @admin.display(description='Imagen')
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height:50px;"/>', obj.image.url)
        return '-'
