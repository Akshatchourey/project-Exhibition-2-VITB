from django.shortcuts import render, redirect
from .models import Blog, BlogComment
from django.contrib.auth.decorators import login_required
from math import ceil as c

# Create your views here.
@login_required(login_url='/login/')
def your_blogs(request):
    no_of_posts = 6
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)
    blogs = Blog.objects.filter(owner=request.user)
    length = len(blogs)
    blogs = blogs[(page-1)*no_of_posts: page*no_of_posts]
    if page > 1:
        prev = page-1
    else:
        prev = None
    if page < c(length/no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    context = {'blogs': blogs, 'prev': prev, 'nxt': nxt}
    return render(request, 'content/blogs.html', context)
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
    context = {'post': this_blog}
    if this_blog:
        this_blog.views += 1
        this_blog.save()

    if request.method == "POST":
        comment = request.POST.get("new_comment")
        blog_comment = BlogComment(blog=this_blog, name=request.user, body=comment)
        blog_comment.save()

        return render(request, 'content/blogpost.html', context)

    return render(request, 'content/blogpost.html', context)
