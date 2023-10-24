#page containing the urls that helps the user to navigate between pages
from django.urls import path
from . import views

urlpatterns = [
    path('', views.JobListView.as_view(), name='listing'),
    path('new/', views.JobCreateView.as_view(), name='newuser'),
    path('edit/<int:pk>/', views.JobUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.JobDeleteView.as_view(), name='delete'),
]