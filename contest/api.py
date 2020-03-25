from .models import ClassFile, ClassContest
from rest_framework import viewsets, permissions
from .serializers import ContestSerializer, FileSerializer


class FileAPI(viewsets.ModelViewSet):
    queryset = ClassFile.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FileSerializer


class ContestAPI(viewsets.ModelViewSet):
    queryset = ClassContest.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ContestSerializer
