from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    try:
       admins = Admin.objects.get(username = request.user.id)
    except:
        admins = None

    return render(request, 'main/home.html', {'username': request.user.username, 'admins':admins})






@login_required
def create_application(request):
    if request.POST:
        form = CreateApplication(request.POST)
        if form.is_valid():
            new_application = Application(worker = Worker.objects.get(username = request.user.id), title = request.POST.get('title'), description = request.POST.get('description'), start_date = request.POST.get('start_date'), end_date = request.POST.get('end_date'))
            new_application.save()
            record = Record.objects.get(username = request.user.id)
            record.total = record.total + 1
            record.last_date = new_application.date_created
            record.save()
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
def delete_application_pending(request, pk = None):
    application = Application.objects.get(id = pk)
    application.delete()
    return redirect('pending-application')

@login_required
def delete_application_accepted(request, pk = None):
    application = Application.objects.get(id = pk)
    application.delete()
    return redirect('accepted-application')

@login_required
def delete_application_rejected(request, pk = None):
    application = Application.objects.get(id = pk)
    application.delete()
    return redirect('rejected-application')

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
def view_record(request):
    record = Record.objects.get(username = request.user.id)
    return render(request, 'main/view_record.html', {'record': record})









@login_required
def check_application(request):
    return render(request, 'main/check_application.html', {'applications': Application.objects.filter(status = "Pending")})

@login_required
def accept_application(request, pk = None, name = None):
   application = Application.objects.get(id = pk)
   employee = User.objects.get(username = name)
   record = Record.objects.get(username = employee.id)
   if application.status == "Pending" or "Rejected":
      application.status = "Accepted"
      application.save()
      record.accepted = record.accepted + 1
      record.save()
   return redirect('check-application')

@login_required
def reject_application(request, pk = None, name = None):
   application = Application.objects.get(id = pk)
   employee = User.objects.get(username = name)
   record = Record.objects.get(username = employee.id)
   if application.status == "Pending" or "Accepted":
      application.status = "Rejected"
      application.save()
      record.rejected = record.rejected + 1
      record.save()
   return redirect('check-application')

@login_required
def register_worker(request):
    if request.POST:
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            new_worker = Worker(username = User.objects.get(username = request.POST.get('username','username')), first_name = "Not added", last_name = "Not added", phone = "Not added", email = "Not added", address = "Not added")
            new_worker.save()
            record = Record(username = User.objects.get(username = request.POST.get('username', 'username')))
            record.save()
            messages.success(request,f"User {request.POST['username']} added successfully")
            return render(request, 'main/register_worker.html', {'form':form})
        else:
            messages.error(request,f"Please enter the details correctly and Make sure that user does not exist already!!")
            return render(request, 'main/register_worker.html', {'form':form})

    form = UserRegistrationForm()
    return render(request, 'main/register_worker.html', {'form':form})

@login_required
def view_employee(request):
    workers = Worker.objects.all()
    return render(request, 'main/view_employee.html', {'workers': workers})

@login_required
def delete_employee(request, pk=None):
    worker = User.objects.get(username = pk)
    worker.delete()
    return redirect('view-employee')

@login_required
def register_admin(request):
    if request.POST:
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            new_worker = Admin(username = User.objects.get(username = request.POST.get('username','username')))
            new_worker.save()
            messages.success(request,f"Admin {request.POST['username']} added successfully")
        else:
            messages.error(request,f"Please enter the details correctly and make sure user does not exist already!!")

    form = UserRegistrationForm()
    return render(request, 'main/register_admin.html', {'form':form})

@login_required
def view_admin(request):
    admins = Admin.objects.all()
    return render(request, 'main/view_admin.html', {'admins': admins})

@login_required
def delete_admin(request, pk=None):
    admin = User.objects.get(username = pk)
    admin.delete()
    return redirect('view-admin')

@login_required
def view_record_admin(request):
    record = Record.objects.all()
    return render(request, 'main/view_record_admin.html', {'records': record})