from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from rest_framework import routers

urlpatterns = [
    path('check_admin_or_not/', check_admin_or_not),
    path('admin_password_change/', admin_password_change),

]


