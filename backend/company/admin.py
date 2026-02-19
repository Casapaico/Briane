from django.contrib import admin
from django.utils.html import format_html

from .models import CompanyInfo, Stat, TeamMember, Client, NewsArticle


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General', {'fields': ['name', 'tagline', 'description']}),
        ('Mision y Vision', {'fields': ['mission', 'vision', 'values']}),
        ('Contacto', {'fields': ['address', 'phones', 'emails', 'hours', 'whatsapp_number']}),
        ('Web', {'fields': ['social_links', 'google_maps_embed_url']}),
    ]

    def has_add_permission(self, request):
        return not CompanyInfo.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ['value', 'label', 'suffix', 'order', 'is_active']
    list_editable = ['order', 'is_active']


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'image_preview', 'order', 'is_active']
    list_editable = ['order', 'is_active']

    @admin.display(description='Foto')
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height:50px;"/>', obj.image.url)
        return '-'


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'logo_preview', 'url', 'order', 'is_active']
    list_editable = ['order', 'is_active']

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
