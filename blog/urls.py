from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('bugs', views.bugs, name='blog-bugs'),
    path('contact', views.contact, name='blog-contact'),
    path('all_bugs', views.bugs, name='blog-all_bugs'),

]
