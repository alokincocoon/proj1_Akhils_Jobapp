from django.urls import path
from . import views

urlpatterns = [
    path('', views.listing, name='listing'),
    path('new/', views.new_user, name='newuser'),
    path('edit/', views.EditTask, name='edit'),
    path('delete/',views.deleteData,name='delete')
   
]