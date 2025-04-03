from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Blog
from .decorators import allowed_users

# Create your views here.
@login_required(login_url='/login/')
def profile(request):
    return render(request, 'content/profile.html')

@login_required(login_url='/login/')
def create_blog(request):
    if request.method == "POSt":
        title = request.POST.get('blog_title')
        content = request.POST.get('main_content')

        new_blog = Blog()
        new_blog.save()
        return redirect(request, "/your_blogs/")

    return render(request, 'content/blogcreate.html')
