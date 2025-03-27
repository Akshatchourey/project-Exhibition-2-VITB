from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    slug = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    # thumbnail = models.ImageField(max_length=300)
    content = models.TextField()
    views = models.PositiveIntegerField()
    likes = models.PositiveIntegerField()

    def __str__(self):
        return self.title
class Video(models.Model):
    sno = models.AutoField(primary_key=True)
    pf = models.CharField(max_length=1)
    title = models.CharField(max_length=200)
    visible = models.BooleanField()  # visibility 1-visible
    desc = models.TextField()
    thumbnail = models.ImageField(upload_to ='video_thumbnail/')
    date = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField()
    likes = models.PositiveIntegerField()
    slug = models.CharField(max_length=25)
    source = models.CharField(max_length=300)

    def __str__(self):
        return self.slug


class Playlist(models.Model):
    sno = models.AutoField(primary_key=True)
    pf = models.CharField(max_length=1)
    title = models.CharField(max_length=200)
    visible = models.BooleanField()  # visibility 1-visible
    desc = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to ='playlist_thumbnail/')
    slug = models.CharField(max_length=25)

    def __str__(self):
        return self.slug
