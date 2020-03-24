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

    path('contest/all/', get_all_contest),
    path('contest/get/', get_contest),
    path('get_file/', get_file),


   # path('image/add/', add_image),x

] \
              #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += router.urls

