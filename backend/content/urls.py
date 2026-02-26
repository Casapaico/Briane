from django.urls import path

from . import views

urlpatterns = [
    path('gallery/<slug:category>/', views.GalleryImageListView.as_view(), name='gallery'),
    path('page-content/<slug:page_slug>/<str:section_key>/', views.PageContentDetailView.as_view(), name='page-content'),
]
