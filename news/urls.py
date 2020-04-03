from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from rest_framework import routers
from .api import NewsAPI, ImageAPI

router = routers.DefaultRouter()

router.register('api/img', ImageAPI, 'image')
router.register('api/news', NewsAPI, 'news')

urlpatterns = [
    path('all/', get_all_news),
    path('add/', add_news),
    path('image/all/', get_all_image),
    path('news_detail/', news_detail),
    path('news_detail/<int:pk>', news_detail),
]
urlpatterns += router.urls

