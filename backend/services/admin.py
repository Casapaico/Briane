from django.contrib import admin
from django.utils.html import format_html

from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image_preview', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    prepopulated_fields = {'slug': ('name',)}

    @admin.display(description='Imagen')
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height:50px;"/>', obj.image.url)
        return '-'
