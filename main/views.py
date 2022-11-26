from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    return render(request, 'main/home.html', {'username': request.user.username})

@login_required
def create_application(request):
    if request.POST:
        form = CreateApplication(request.POST)
        if form.is_valid():
            new_application = Application(worker = Worker.objects.get(username = request.user.id), title = request.POST.get('title', 'title'), description = request.POST.get('description', 'description'))
            new_application.save()
        messages.success(request,f"Application sent successfully")
    
    form = CreateApplication()
    return render(request, 'main/create_application.html', {'form': form})

@login_required
def pending_applications(request):
    return render(request, 'main/pending_applications.html', {'applications': Application.objects.filter(worker = Worker.objects.get(username = request.user.id))})

@login_required
def accepted_applications(request):
    return render(request, 'main/accepted_applications.html', {'applications': Application.objects.filter(worker = Worker.objects.get(username = request.user.id))})

@login_required
def rejected_applications(request):
    return render(request, 'main/rejected_applications.html', {'applications': Application.objects.filter(worker = Worker.objects.get(username = request.user.id))})

@login_required
def delete_application(request, pk = None):
    application = Application.objects.get(id = pk)
    application.delete()
    return redirect('pending-application')

@login_required
def edit_details(request):

    if request.POST:
        form = UserDetailsForm(request.POST)
       
        if form.is_valid():
            worker = Worker.objects.get(username = request.user)
            worker.first_name = request.POST.get("first_name")
            worker.last_name = request.POST.get("last_name")
            worker.phone = request.POST.get("phone")
            worker.email = request.POST.get("email")
            worker.address = request.POST.get("address")
            worker.save()
            messages.success(request, f"Details changed successfully")
        else:
            messages.error(request, f"Could not change details. Please enter correct details.")
    
    worker = Worker.objects.get(username = request.user.id)
    return render(request, 'main/edit_details.html', {'worker': worker})







@login_required
def check_application(request):
    return render(request, 'main/check_application.html', {'applications': Application.objects.filter(status = "Pending")})

@login_required
def accept_application(request, pk = None):
   application = Application.objects.get(id = pk)
   if application.status == "Pending" or "Rejected":
      application.status = "Accepted"
      application.save()
   return redirect('check-application')

@login_required
def reject_application(request, pk = None):
   application = Application.objects.get(id = pk)
   if application.status == "Pending" or "Accepted":
      application.status = "Rejected"
      application.save()
   return redirect('check-application')

@login_required
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

@login_required
def view_employee(request):
    workers = Worker.objects.all()
    return render(request, 'main/view_employee.html', {'workers': workers})

@login_required
def delete_employee(request, pk=None):
    worker = User.objects.get(username = pk)
    worker.delete()
    return redirect('view-employee')