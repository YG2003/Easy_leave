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

def pending_applications(request):
    return render(request, 'main/pending_applications.html', {'applications': Application.objects.filter(worker = Worker.objects.get(username = request.user.username))})

def accepted_applications(request):
    return render(request, 'main/accepted_applications.html', {'applications': Application.objects.filter(worker = Worker.objects.get(username = request.user.username))})

def rejected_applications(request):
    return render(request, 'main/rejected_applications.html', {'applications': Application.objects.filter(worker = Worker.objects.get(username = request.user.username))})

def delete_application(request, pk = None):
    application = Application.objects.get(id = pk)
    application.delete()
    return redirect('pending-application')


a = 0  

def edit_details(request):

    if request.POST:
        form = UserDetailsForm(request.POST)
        a = 1
        if form.is_valid():
            worker = Worker.objects.get(username = request.user)
            worker.first_name = request.POST.get('first_name', 'first_name')
            worker.last_name = request.POST.get('last_name', 'last_name')
            worker.phone = request.POST.get('phone', 'phone')
            worker.email = request.POST.get('email', 'email')
            worker.address = request.POST.get('address', 'address')
            worker.save()
            messages.success(request, f"Details changed successfully")
        else:
            messages.error(request, f"Could not change details. Please enter correct details.")
    if a == 0:
       form = UserDetailsForm()
    return render(request, 'main/edit_details.html', {'form': form})








def check_application(request):
    return render(request, 'main/check_application.html', {'applications': Application.objects.filter(status = "Pending")})

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
            new_worker = Worker(username = User.objects.get(username = request.POST.get('username','username')), first_name = "Not added", last_name = "Not added", phone = "Not added", email = "Not added", address = "Not added")
            new_worker.save()
            messages.success(request,f"User {request.POST['username']} added successfully")
        else:
            messages.error(request,f"Please enter the details correctly!!")

    form = UserRegistrationForm()
    return render(request, 'main/register.html', {'form':form})