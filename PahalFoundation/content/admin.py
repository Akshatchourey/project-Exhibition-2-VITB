from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Blog)
admin.site.register(BlogComment)
admin.site.register(Video)
admin.site.register(Playlist)

admin.site.register(Student)
admin.site.register(Volunteer)
