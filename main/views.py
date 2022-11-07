from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *


# Create your views here.

def create_application(request):
    if request.POST:
        form = CreateApplication(request.POST)
        if form.is_valid():
            new_application = Application(worker = request.POST.get('worker', Worker.objects.get(id = '1')), title = request.POST.get('title', 'title'), description = request.POST.get('description', 'description'))
            new_application.save()
        messages.success(request,f"Application sent successfully")
    
    form = CreateApplication()
    return render(request, 'worker_home.html', {'form': form, 'applications': Application.objects.all()})

def manager_home(request):
    return render(request, 'manager_home.html', {'applications': Application.objects.all()})

def accept_application(request, pk = None):
   application = Application.objects.get(id = pk)
   if application.status == "Pending" or "Rejected":
      application.status = "Accepted"
      application.save()
   return redirect('manager-home')

def reject_application(request, pk = None):
   application = Application.objects.get(id = pk)
   if application.status == "Pending" or "Accepted":
      application.status = "Rejected"
      application.save()
   return redirect('manager-home')
    
def register(request):
    if request.POST:
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            if request.POST.get('position', 'position') == "Manager":
                new_manager = Manager(username = request.POST.get('username', 'username'), password = request.POST.get('password', 'password'), email = request.POST.get('email', 'email'), phone = request.POST.get('phone', 'phone'))
                new_manager.save()
            elif request.POST.get('position', 'position') == "Worker":
                new_worker = Worker(username = request.POST.get('username', 'username'), password = request.POST.get('password', 'password'), email = request.POST.get('email', 'email'), phone = request.POST.get('phone', 'phone'))
                new_worker.save()
        messages.success(request,f"User {request.POST['username']} added successfully as {request.POST['position']}")

    form = UserRegistrationForm()
    return render(request, 'register.html', {'form':form})