from django.urls import path

from . import views

urlpatterns = [
    path('company-info/', views.CompanyInfoView.as_view(), name='company-info'),
    path('stats/', views.StatListView.as_view(), name='stats-list'),
    path('team/', views.TeamMemberListView.as_view(), name='team-list'),
    path('clients/', views.ClientListView.as_view(), name='clients-list'),
    path('news/', views.NewsArticleListView.as_view(), name='news-list'),
    path('news/<slug:slug>/', views.NewsArticleDetailView.as_view(), name='news-detail'),
]
