from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('bugs', views.bugs, name='blog-bugs'),
]
