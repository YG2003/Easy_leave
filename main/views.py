from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *


# Create your views here.

def home(request):
    return render(request, 'main/home.html', {'username': request.user.username})


def create_application(request):
    if request.POST:
        form = CreateApplication(request.POST)
        if form.is_valid():
            new_application = Application(worker = Worker.objects.get(username = request.user.username), title = request.POST.get('title', 'title'), description = request.POST.get('description', 'description'))
            new_application.save()
        messages.success(request,f"Application sent successfully")
    
    form = CreateApplication()
    return render(request, 'main/create_application.html', {'form': form})

def view_applications(request):
    return render(request, 'main/view_applications.html', {'applications': Application.objects.filter(worker = Worker.objects.get(username = request.user.username))})


def check_application(request):
    return render(request, 'main/manager_home.html', {'applications': Application.objects.filter(status = "Pending")})

def accept_application(request, pk = None):
   application = Application.objects.get(id = pk)
   if application.status == "Pending" or "Rejected":
      application.status = "Accepted"
      application.save()
   return redirect('check-application')

def reject_application(request, pk = None):
   application = Application.objects.get(id = pk)
   if application.status == "Pending" or "Accepted":
      application.status = "Rejected"
      application.save()
   return redirect('check-application')


def register(request):
    if request.POST:
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            new_worker = Worker(username = request.POST.get('username', 'username'))
            new_worker.save()
            messages.success(request,f"User {request.POST['username']} added successfully")

    form = UserRegistrationForm()
    return render(request, 'main/register.html', {'form':form})