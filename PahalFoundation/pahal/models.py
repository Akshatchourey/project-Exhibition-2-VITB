from django.db import models

# Create your models here.

class NewVolunteer(models.Model):
    sno = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    fullName = models.CharField(max_length=100)
    email = models.EmailField(max_length=120)
    phoneNo = models.CharField(max_length=12)
    interestArea = models.TextField()
    about = models.TextField()

    def __str__(self):
        return self.fullName

class ContactUs(models.Model):
    sno = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    fullName = models.CharField(max_length=100)
    email = models.EmailField(max_length=120)
    phoneNo = models.CharField(max_length=12)
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.fullName
