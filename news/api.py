from .models import ClassImage, ClassNews
from rest_framework import viewsets, permissions
from .serializers import ImageSerializer, NewsSerializer


class ImageAPI(viewsets.ModelViewSet):
    queryset = ClassImage.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ImageSerializer


class NewsAPI(viewsets.ModelViewSet):
    queryset = ClassNews.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = NewsSerializer
