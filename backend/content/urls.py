from django.urls import path

from . import views

urlpatterns = [
    path('gallery/<slug:category>/', views.GalleryImageListView.as_view(), name='gallery'),
]
