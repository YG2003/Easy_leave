from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Worker(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 50, verbose_name = "First Name")
    last_name = models.CharField(max_length = 50, verbose_name = "Last Name")
    phone = models.CharField(max_length = 10, verbose_name = "Mobile number")
    email = models.EmailField(verbose_name = "Email")
    address = models.TextField(verbose_name = "Address")
    
    
    def __str__(self):
        worker = str(self.username)
        return worker

class Application(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    title = models.CharField(max_length = 50, verbose_name = "Title")
    description = models.TextField(verbose_name = "Description")
    date_created = models.DateField(verbose_name = "Date created", auto_now_add=True)
    start_date = models.DateField(verbose_name = "Start date of leave", null = True)
    end_date = models.DateField(verbose_name = "End date of leave", null = True)
    status_choices = (
        ("Pending", "Pending"),
        ("Accepted", "Accepted"),
        ("Rejected", "Rejected"),
    )
    status = models.CharField(max_length = 20, choices = status_choices, default = "Pending")

    def __str__(self):
        return self.title

class Admin(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        worker = str(self.username)
        return worker

class Record(models.Model):
    username = models.ForeignKey(User, on_delete= models.CASCADE)
    total = models.IntegerField(verbose_name = "Total applications sent", default = 0)
    accepted = models.IntegerField(verbose_name = "Accepted applications", default = 0)
    rejected = models.IntegerField(verbose_name = "Rejected Applications", default = 0)
    last_date = models.DateField(verbose_name = "Last application sent on", null=True)

    def __str__(self):
        return(str(self.username))
