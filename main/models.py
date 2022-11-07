from django.db import models

# Create your models here.

class Worker(models.Model):
    username = models.CharField(max_length = 30, verbose_name = "Username")
    password = models.CharField(max_length = 30, verbose_name = "Password")
    email = models.EmailField(verbose_name="Email")
    phone = models.IntegerField(verbose_name="Phone Number")

    def __str__(self):
        return self.username

class Manager(models.Model):
    username = models.CharField(max_length = 30, verbose_name = "Username")
    password = models.CharField(max_length = 30, verbose_name = "Password")
    email = models.EmailField(verbose_name="Email")
    phone = models.IntegerField(verbose_name="Phone Number")

    def __str__(self):
        return self.username

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