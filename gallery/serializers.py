from rest_framework import serializers
from .models import ClassGallery


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassGallery
        fields = '__all__'


