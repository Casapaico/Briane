from django.contrib import admin
from django.utils.html import format_html

from .models import CompanyInfo, Stat, TeamMember, Client, NewsArticle


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General', {'fields': ['name', 'tagline', 'description']}),
        ('Mision y Vision', {'fields': ['mission', 'vision', 'values']}),
        ('Contacto', {'fields': ['address', 'phones', 'emails', 'hours', 'whatsapp_number']}),
        ('Web y Redes', {'fields': ['social_links', 'google_maps_embed_url']}),
    ]

    def has_add_permission(self, request):
        return not CompanyInfo.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ['value', 'label', 'suffix', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    search_fields = ['label']


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'image_preview', 'is_active', 'order']
    list_filter = ['is_active']
    search_fields = ['name', 'position']
    list_editable = ['is_active', 'order']
    fieldsets = [
        ('Informacion', {'fields': ['name', 'position', 'bio']}),
        ('Imagen', {'fields': ['image']}),
        ('Opciones', {'fields': ['is_active', 'order']}),
    ]

    @admin.display(description='Foto')
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height:50px;border-radius:50%;"/>', obj.image.url)
        return '-'


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'logo_preview', 'url', 'is_active', 'order']
    list_filter = ['is_active']
    search_fields = ['name']
    list_editable = ['is_active', 'order']

    @admin.display(description='Logo')
    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="max-height:40px;"/>', obj.logo.url)
        return '-'


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
