from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    slug = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    content = CKEditor5Field('Text', config_name='extends')
    views = models.PositiveIntegerField()
    likes = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class BlogComment(models.Model):
    blog = models.ForeignKey(Blog, related_name="blogComment", on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s - %s" % (self.blog.title, self.name)

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

class Student(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    active = models.BooleanField(default=1)
    name = models.CharField(max_length=70)
    parents_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=12)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to ='students/')

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="attendances")
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10)

    class Meta:
        unique_together = ('student', 'date')

class Volunteer(models.Model):
    Reg_no = models.CharField(primary_key=True, max_length=70)
    name = models.CharField(unique=True, null=False, max_length=70)
    designation = models.CharField(max_length=25)
    email = models.EmailField(max_length=80)
    phone_no = models.CharField(max_length=12)
    photo = models.ImageField(upload_to ='volunteer/')
