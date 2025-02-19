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
