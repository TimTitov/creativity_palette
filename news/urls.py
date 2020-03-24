from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from rest_framework import routers
from .api import TestViewSet, FileAPIViewSet, ContestAPIViewSet

router = routers.DefaultRouter()

router.register('api/img', TestViewSet, 'img')
router.register('api/file', FileAPIViewSet, 'file')
router.register('api/file', FileAPIViewSet, 'file')
router.register('api/contest', ContestAPIViewSet, 'contest')

urlpatterns = [
    path('all/', get_all_news),
    path('add/', add_news),
    path('image/all/', get_all_image),
    path('contest/all/', get_all_contest),
    path('contest/get/', get_contest),
    path('get_file/', get_file),


   # path('image/add/', add_image),x

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += router.urls

