from rest_framework import serializers
from .models import ClassNews, ClassImage


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassNews
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassImage
        fields = '__all__'

