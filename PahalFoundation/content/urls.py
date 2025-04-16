from django.urls import path
from .import views
from .import views_videos as views2
from .import views_teacher as views3



urlpatterns = [
    # views
    path('blogs/', views.blog, name='blog'),
    path('blogpost/<str:slug>', views.blogpost, name='blogpost'),
    path('your_blogs/', views.your_blogs, name='your_blogs'),
    # path('gallery/', views.gallery, name='gallery'),

    # views2
    path('videos/', views2.video, name='video'),
    path('video_playing/<str:slug>', views2.video_playing, name='video_playing'),
    path('playlists/', views2.playlist, name='playlist'),
    path('playlist/<str:slug>', views2.plvideos, name='video_in_playlist'),

    # views3
    path('dashboard/profile/', views3.profile, name="profile"),
    path('dashboard/timetable/', views3.timetable, name="timetable"),
    path('dashboard/student-info/', views3.student_info, name="student_info"),
    path('dashboard/attendance/', views3.attendance, name="attendance"),
    path('dashboard/admission/',views3.admission,name="admission"),
    path('dashboard/volunteer-info/', views3.volunteer_info, name="volunteer_info"),
    path('dashboard/volunteer-enrolment/',views3.volunteer_enrolment,name="volunteer_enrolment"),
    path('dashboard/create_blog/',views3.create_blog,name="create_blog"),

]
