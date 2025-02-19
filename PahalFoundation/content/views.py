from django.shortcuts import render
from .models import Blog
from math import ceil as c

# Create your views here.
def blog(request):
    no_of_posts = 6
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)
    blogs = Blog.objects.all()
    length = len(blogs)
    blogs = blogs[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev=page-1
    else:
        prev = None
    if page < c(length/no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    context = {'blogs': blogs, 'prev': prev, 'nxt': nxt}
    return render(request, 'content/blogs.html', context)

def blogpost(request, slug):
    this_blog = Blog.objects.filter(slug=slug).first()
    context = {'name': this_blog}
    return render(request, 'content/blogpost.html', context)
