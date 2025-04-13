from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Blog, Student, Attendance
from .forms import WriteBlog, Admission, VolunteerEnrolment
from .decorators import allowed_users

# Create your views here.
@login_required(login_url='/login/')
def profile(request):
    return render(request, 'content/profile.html')

@login_required(login_url='/login/')
def timetable(request):
    return render(request, 'content/timetable.html')

@login_required(login_url='/login/')
def create_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Blog.objects.create(owner=request.user,
                            title=title, content=content, views=0, likes=0)
        return redirect("/your_blogs")
    return render(request, 'content/blogcreate.html')


@allowed_users(allowed_roles=['teacher', 'admin'])
def student_info(request):
    students = Student.objects.filter()
    return render(request, 'content/students_info.html', {"students":students})

@allowed_users(allowed_roles=['teacher','admin'])
def attendance(request):
    students = Student.objects.filter(active=1)

    if request.method == "POST":
        for st in students:
            status = request.POST.get("rollNo" + str(st.roll_no))
            att = Attendance(student=st, status=status)
            att.save()

        return redirect("/dashboard/attendance")

    return render(request, 'content/attendance.html',{"students":students})

@allowed_users(allowed_roles=['teacher','admin'])
def admission(request):
    if request.method == 'POST':
        form = Admission(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'content/admission.html')

@allowed_users(allowed_roles=['admin'])
def volunteer_enrolment(request):
    if request.method == 'POST':
        form = VolunteerEnrolment(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'content/volunteer_enrolment.html')
