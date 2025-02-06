from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, 'pahal/aboutUs.html')
def gallery(request):
    return render(request, 'pahal/gallery.html')
def volunteer(request):
    return render(request, 'pahal/volunteer.html')
def get_involved(request):
    return render(request, 'pahal/get_involved.html')
def contact(request):
    return render(request, 'pahal/contactUs.html')
def donate(request):
    return render(request, 'pahal/donate.html')