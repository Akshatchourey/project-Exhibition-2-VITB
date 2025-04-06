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
            'content': forms.Textarea(attrs={'placeholder': 'Write your blog content here'}),
        }

    content = forms.CharField(widget=CKEditor5Widget)
