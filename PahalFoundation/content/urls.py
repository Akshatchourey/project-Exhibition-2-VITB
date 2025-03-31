from django.urls import path
from .import views
from .import views_videos as views2
from .import views_teacher as views3

urlpatterns = [
    # views
    path('blogs/', views.blog, name='blog'),
    path('blogpost/<str:slug>', views.blogpost, name='blogpost'),
    # path('gallery/', views.gallery, name='gallery'),

    # views2
    path('videos/', views2.video, name='video'),
    path('video_playing/<str:slug>', views2.video_playing, name='video_playing'),
    path('playlists/', views2.playlist, name='playlist'),
    path('playlist/<str:slug>', views2.plvideos, name='video_in_playlist'),

    # views3
    path('create_blog/',views3.create_blog,name="create_blog"),
]
