from django.urls import path
from .import views
from .import views_main_pages as views2
from .import views_teacher as views3

urlpatterns = [
    # views
    path('', views.index, name='pahal'),
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('change_password/', views.change_password, name='change_password'),
    path('error404/', views.error_page, name='error404'),

    # views2
    path('about/', views2.about, name='about'),
    path('volunteer/', views2.volunteer, name='volunteer'),
    path('get_involved/', views2.get_involved, name='get_involved'),
    path('contact/', views2.contact, name='contact'),
    path('donate/', views2.donate, name='donate'),

    # views3

]
