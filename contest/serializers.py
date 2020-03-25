from rest_framework import serializers
from .models import ClassContest, ClassFile


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassFile
        fields = '__all__'


class ContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassContest
        fields = '__all__'
