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
    path('delete_application_pending/<int:pk>', delete_application_pending, name = "delete-application-pending"),
    path('delete_application_accepted/<int:pk>', delete_application_accepted, name = "delete-application-accepted"),
    path('delete_application_rejected/<int:pk>', delete_application_rejected, name = "delete-application-rejected"),
    path('check_application', check_application, name = "check-application"),
    path('accept_application/<int:pk>/<str:name>', accept_application, name = "accept-application"),
    path('reject_application/<int:pk>/<str:name>', reject_application, name = "reject-application"),
    path('register_worker', register_worker, name = "register-worker"),
    path('', views.LoginView.as_view(template_name = "main/login.html"), name = "login"),
    path('logout', views.LogoutView.as_view(template_name = "main/logout.html"), name = "logout"),
    path('home', home, name = "home"),
    path('view_employee', view_employee, name = "view-employee"),
    path('delete_employee/<str:pk>', delete_employee, name = "delete-employee"),
    path('register_admin', register_admin, name = "register-admin"),
    path('view_admin', view_admin, name = "view-admin"),
    path('delete_admin/<str:pk>', delete_admin, name = "delete-admin"),
    path('view_record', view_record, name = "view-record"),
    path('view_record_admin', view_record_admin, name = "view-record-admin"),

]