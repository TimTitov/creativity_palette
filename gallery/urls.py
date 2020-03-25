from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from rest_framework import routers
from .api import GalleryAPI

router = routers.DefaultRouter()

router.register('api/gallery', GalleryAPI, 'gallery')

urlpatterns = [
    # path('add/', add_in_gallery),
    # path('add/', add_in_gallery),
    # path('add/', add_news),
    # path('image/all/', get_all_image),
    # path('contest/all/', get_all_contest),
    # path('contest/get/', get_contest),
    # path('get_file/', get_file),
]
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += router.urls

