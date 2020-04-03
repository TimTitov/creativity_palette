from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .views import *
from .api import ContestAPI, FileAPI

router = routers.DefaultRouter()


router.register('api/file', FileAPI, 'file')
router.register('api/contest', ContestAPI, 'contest')

urlpatterns = [
    path('all/', get_all_contest),
    path('get/', get_contest),
    path('add/', add_contest),
    path('get_file/', get_file),
    path('contest_detail/', contest_detail),
    path('contest_detail/<int:pk>', contest_detail),
]
urlpatterns += router.urls

