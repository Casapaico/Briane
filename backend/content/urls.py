from django.urls import path

from . import views

urlpatterns = [
    path('pages/<slug:slug>/', views.PageContentListView.as_view(), name='page-content'),
    path('pages/<slug:slug>/images/', views.PageImageListView.as_view(), name='page-images'),
    path('gallery/<slug:category>/', views.GalleryImageListView.as_view(), name='gallery'),
]
