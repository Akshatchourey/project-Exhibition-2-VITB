from django.shortcuts import render, redirect
from django.utils.text import slugify
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.decorators import login_required
from .models import Blog, Student, Attendance, Volunteer
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
    form = WriteBlog()
    if request.method == 'POST':
        form = WriteBlog(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.owner = request.user
            blog.slug = slugify(blog.title)
            blog.views = blog.likes = 0
            blog.save()
            return redirect("/your_blogs")
        else:
            messages.error(request, "Form is showing invalid.")

    return render(request, 'content/blogcreate.html', {"form":form})


@allowed_users(allowed_roles=['teacher', 'admin'])
def student_info(request):
    students = Student.objects.filter()
    return render(request, 'content/students_info.html', {"students":students})

@allowed_users(allowed_roles=['teacher','admin'])
def attendance(request):
    students = Student.objects.filter(active=1)

    if request.method == "POST":
        try:
            with transaction.atomic():
                for st in students:
                    status = request.POST.get("rollNo" + str(st.roll_no))
                    att = Attendance(student=st, status=status)
                    att.save()
            return redirect("/dashboard/profile")
        except Exception as e:
            # Rollback transaction and display error message
            messages.error(request, "Unable to save attendance: " + str(e))

    return render(request, 'content/attendance.html',{"students":students})

@allowed_users(allowed_roles=['teacher','admin'])
def admission(request):
    if request.method == 'POST':
        form = Admission(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/student-info')
        else:
            messages.error(request, "Admission form is showing invalid.")
    return render(request, 'content/admission.html')

@allowed_users(allowed_roles=['admin'])
def volunteer_info(request):
    volunteer = Volunteer.objects.filter()
    return render(request, 'content/volunteer_info.html', {'volunteer':volunteer})
@allowed_users(allowed_roles=['admin'])
def volunteer_enrolment(request):
    if request.method == 'POST':
        form = VolunteerEnrolment(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/volunteer-info')
        else:
            messages.error(request, "Volunteer enrolment form is showing invalid.")
    return render(request, 'content/volunteer_enrolment.html')
