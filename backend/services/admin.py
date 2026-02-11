from django.contrib import admin
from django.utils.html import format_html

from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image_preview', 'is_active', 'order']
    list_filter = ['is_active']
    search_fields = ['name', 'short_description', 'description']
    list_editable = ['is_active', 'order']
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = [
        ('Informacion', {'fields': ['name', 'slug', 'icon']}),
        ('Descripcion', {'fields': ['short_description', 'description', 'features']}),
        ('Imagen', {'fields': ['image']}),
        ('Opciones', {'fields': ['is_active', 'order']}),
    ]

    @admin.display(description='Vista previa')
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height:50px;"/>', obj.image.url)
        return '-'
