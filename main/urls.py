from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('worker_home', create_application, name = "worker-home"),
    path('manager_home', manager_home, name = "manager-home"),
    path('accept_application/<int:pk>', accept_application, name = "accept-application"),
    path('reject_application/<int:pk>', reject_application, name = "reject-application"),
    path('register', register, name = "register")
]