from django.urls import path
from .import views

urlpatterns = [
    # views
    path('blogs/', views.blog, name='blog'),
    path('blogpost/<str:slug>', views.blogpost, name='blogpost'),
]
