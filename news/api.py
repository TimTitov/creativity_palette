from .models import ImageModel, FeedFile, Contest
from rest_framework import viewsets, permissions
from .serializers import ImageSerializer, FileSerializer, ConrestSerializer


class TestViewSet(viewsets.ModelViewSet):
    queryset = ImageModel.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ImageSerializer


class FileAPIViewSet(viewsets.ModelViewSet):
    queryset = FeedFile.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FileSerializer


class ContestAPIViewSet(viewsets.ModelViewSet):
    queryset = Contest.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ConrestSerializer
