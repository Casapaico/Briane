from django.contrib import admin
from django.utils.html import format_html

from .models import PageContent, PageImage, GalleryImage


@admin.register(PageContent)
class PageContentAdmin(admin.ModelAdmin):
    list_display = ['page_slug', 'section_key', 'title', 'is_active', 'order']
    list_filter = ['page_slug', 'is_active']
    search_fields = ['page_slug', 'section_key', 'title', 'content']
    list_editable = ['is_active', 'order']
    fieldsets = [
        ('Ubicacion', {'fields': ['page_slug', 'section_key']}),
        ('Contenido', {'fields': ['title', 'content']}),
        ('Opciones', {'fields': ['is_active', 'order']}),
    ]


@admin.register(PageImage)
class PageImageAdmin(admin.ModelAdmin):
    list_display = ['page_slug', 'section_key', 'image_preview', 'alt_text', 'is_active', 'order']
    list_filter = ['page_slug', 'is_active']
    search_fields = ['page_slug', 'section_key', 'alt_text', 'caption']
    list_editable = ['is_active', 'order']
    fieldsets = [
        ('Ubicacion', {'fields': ['page_slug', 'section_key']}),
        ('Imagen', {'fields': ['image', 'alt_text', 'caption']}),
        ('Opciones', {'fields': ['is_active', 'order']}),
    ]

    @admin.display(description='Vista previa')
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height:50px;"/>', obj.image.url)
        return '-'


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'image_preview', 'person_name', 'year', 'is_active', 'order']
    list_filter = ['category', 'is_active', 'year']
    search_fields = ['title', 'description', 'person_name']
    list_editable = ['is_active', 'order']
    fieldsets = [
        ('Imagen', {'fields': ['category', 'image', 'title', 'description']}),
        ('Persona', {'fields': ['person_name', 'person_comment'], 'classes': ['collapse']}),
        ('Opciones', {'fields': ['year', 'is_active', 'order']}),
    ]

    @admin.display(description='Vista previa')
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height:50px;"/>', obj.image.url)
        return '-'
