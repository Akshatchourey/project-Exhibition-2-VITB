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
    content = CKEditor5Field(config_name='extends')
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
    name = models.CharField(max_length=40)
    parents_name = models.CharField(max_length=40)
    address = models.CharField(max_length=40, blank=True, default='')
    phone_no = models.CharField(max_length=12)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to ='students/', null=True)
    grade = models.CharField(max_length=10, blank=True, default='')
    prev_school = models.CharField(max_length=30, blank=True, default='')

    def __str__(self):
        return "%s. %s" % (self.roll_no, self.name)

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="attendances")
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10)

    class Meta:
        unique_together = ('student', 'date')

    def __str__(self):
        return "%s. %s" % (self.student.name, self.date)

class Volunteer(models.Model):
    Reg_no = models.CharField(primary_key=True, max_length=70)
    name = models.CharField(unique=True, null=False, max_length=70)
    designation = models.CharField(max_length=25)
    email = models.EmailField(max_length=80)
    phone_no = models.CharField(max_length=12)
    photo = models.ImageField(upload_to ='volunteer/', null=True)
    interest = models.CharField(max_length=40, blank=True, default='')
    experience = models.CharField(max_length=40, blank=True, default='')

    def __str__(self):
        return "%s. %s" % (self.name, self.designation)

class Progress(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="progress_repost")
    last_update = models.DateTimeField(auto_now_add=True)
    math = models.CharField(max_length=60, blank=True, null=True)
    hindi = models.CharField(max_length=60, blank=True, null=True)
    english = models.CharField(max_length=60, blank=True, null=True)
    extra_curricular = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return "%s. %s" % (self.student.name, self.last_update)
