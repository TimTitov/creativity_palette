from rest_framework import serializers
from .models import News, ImageModel, FeedFile, Contest


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = '__all__'


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedFile
        fields = '__all__'

class ConrestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contest
        fields = '__all__'

#
# from probably.obtain.models import FileUpload
#
# class FileUploadSerializer(serializers.HyperlinkedModelSerializer):
#     owner = serializers.SlugRelatedField(
#         read_only=True,
#         slug_field='id'
#     )
#
#     class Meta:
#         model = FileUpload
#         read_only_fields = ('created', 'datafile', 'owner')