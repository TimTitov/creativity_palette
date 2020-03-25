from .models import ClassGallery
from rest_framework import viewsets, permissions
from .serializers import GallerySerializer


class GalleryAPI(viewsets.ModelViewSet):
    queryset = ClassGallery.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = GallerySerializer

