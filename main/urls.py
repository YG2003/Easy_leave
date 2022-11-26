from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.auth import views

urlpatterns = [
    path('create_application', create_application, name = "create-application"),
    path('pending_application', pending_applications, name = "pending-application"),
    path('accepted_application', accepted_applications, name = "accepted-application"),
    path('rejected_application', rejected_applications, name = "rejected-application"),
    path('edit_details', edit_details, name = "edit-details"),
    path('delete_application/<int:pk>', delete_application, name = "delete-application"),
    path('check_application', check_application, name = "check-application"),
    path('accept_application/<int:pk>', accept_application, name = "accept-application"),
    path('reject_application/<int:pk>', reject_application, name = "reject-application"),
    path('register', register, name = "register"),
    path('', views.LoginView.as_view(template_name = "main/login.html"), name = "login"),
    path('logout', views.LogoutView.as_view(template_name = "main/logout.html"), name = "logout"),
    path('home', home, name = "home"),
    path('view_employee', view_employee, name = "view-employee"),
    path('delete_employee/<str:pk>', delete_employee, name = "delete-employee"),
]