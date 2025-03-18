from django.urls import path
from .import views
from .import views_teacher as views3

urlpatterns = [
    # views
    path('blogs/', views.blog, name='blog'),
    path('blogpost/<str:slug>', views.blogpost, name='blogpost'),

    # path('videos/', views.videos, name='videos'),
    # path('gallery/', views.gallery, name='gallery'),

    # views3
    path('create_blog/',views3.create_blog,name="create_blog"),
]
