from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Blog, Student, Attendance
from .forms import WriteBlog
from .decorators import allowed_users

# Create your views here.
@login_required(login_url='/login/')
def profile(request):
    return render(request, 'content/profile.html')

@login_required(login_url='/login/')
def create_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Blog.objects.create(owner=request.user,
                            title=title, content=content, views=0, likes=0)
        return redirect("/your_blogs")
    return render(request, 'content/blogcreate.html')

@allowed_users(allowed_roles=['teacher','admin'])
def attendance(request):
    students = Student.objects.filter(active=1)

    if request.method == "POST":
        for st in students:
            status = request.POST.get(st.roll_no)
            # att = Attendance(student=st, status=status)
            # att.save()
            print(status)

        return redirect("/dashboard/attendance")

    return render(request, 'content/attendance.html',{"students":students})

@allowed_users(allowed_roles=['teacher','admin'])
def admission(request):
    return render(request, 'content/admission.html')
