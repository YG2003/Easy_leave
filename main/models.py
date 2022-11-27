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