from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from rest_framework import routers
from .api import GalleryAPI

router = routers.DefaultRouter()

router.register('api/gallery', GalleryAPI, 'gallery')

urlpatterns = router.urls