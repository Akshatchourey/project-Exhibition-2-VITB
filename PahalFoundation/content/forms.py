from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Blog
from .models import Student, Volunteer

class WriteBlog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter blog title'}),
            'content': CKEditor5Widget(attrs={"class": "django_ckeditor_5"}, config_name="extends"),
        }

class Admission(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['active']

class VolunteerEnrolment(forms.ModelForm):
    class Meta:
        model = Volunteer
        exclude = []