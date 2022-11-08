from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.auth import views

urlpatterns = [
    path('create_application', create_application, name = "create-application"),
    path('view_application', view_applications, name = "view-application"),
    path('check_application', check_application, name = "check-application"),
    path('accept_application/<int:pk>', accept_application, name = "accept-application"),
    path('reject_application/<int:pk>', reject_application, name = "reject-application"),
    path('register', register, name = "register"),
    path('', views.LoginView.as_view(template_name = "main/login.html"), name = "login"),
    path('logout', views.LogoutView.as_view(template_name = "main/logout.html"), name = "logout"),
    path('home', home, name = "home"),
]