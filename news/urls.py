from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from rest_framework import routers
from .api import TestViewSet

router = routers.DefaultRouter()

router.register('api/img', TestViewSet, 'img')

urlpatterns = [
    path('all/', get_all_news),
    path('add/', add_news),
    path('image/all/', get_all_image),
   # path('image/add/', add_image),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += router.urls

