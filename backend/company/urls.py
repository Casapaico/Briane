from django.urls import path

from . import views

urlpatterns = [
    path('company/', views.CompanyInfoView.as_view(), name='company-info'),
    path('stats/', views.StatListView.as_view(), name='stat-list'),
    path('team/', views.TeamMemberListView.as_view(), name='team-list'),
    path('clients/', views.ClientListView.as_view(), name='client-list'),
    path('news/', views.NewsArticleListView.as_view(), name='news-list'),
    path('news/<slug:slug>/', views.NewsArticleDetailView.as_view(), name='news-detail'),
]
