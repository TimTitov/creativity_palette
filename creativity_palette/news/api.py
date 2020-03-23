from .models import ImageModel
from rest_framework import viewsets, permissions
from .serializers import ImageSerializer


class TestViewSet(viewsets.ModelViewSet):
    queryset = ImageModel.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ImageSerializer

