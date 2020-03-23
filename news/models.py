from django.db import models


class News(models.Model):
    news_title = models.CharField(max_length=100)
    news_date = models.DateTimeField()
    news_image = models.TextField()
    news_text = models.TextField()

    class Meta:
        verbose_name = 'One News'
        verbose_name_plural = 'News'


class ImageModel(models.Model):
    image_url = models.ImageField(verbose_name='images', upload_to='', blank=True, null=True)
    image_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

#from django.db import models
#from probably.users.models import User


class FileUpload(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    #owner = models.ForeignKey(User, to_field='id')
    datafile = models.FileField()