from django.urls import path

from . import views

urlpatterns = [
    path('contact/', views.ContactSubmissionCreateView.as_view(), name='contact-submit'),
    path('jobs/', views.JobPositionListView.as_view(), name='job-list'),
    path('apply-full/', views.FullJobApplicationCreateView.as_view(), name='job-apply-full'),
    path('newsletter/', views.NewsletterSubscriptionCreateView.as_view(), name='newsletter-subscribe'),
]
