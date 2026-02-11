from django.urls import path

from . import views

urlpatterns = [
    path('news/', views.NewsArticleListView.as_view(), name='news-list'),
    path('news/<slug:slug>/', views.NewsArticleDetailView.as_view(), name='news-detail'),
]
