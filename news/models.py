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

class FileModel(models.Model):
    file_url = models.FileField(verbose_name='files', upload_to='', blank=True, null=True)
    file_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'

 # files: string[];
  #news_title = models.CharField(max_length=100)

    @property
    def files(self):
        list = [{i.file} for i in FeedFile.objects.all()]
        return list

#    news_text = models.TextField()

    # class Meta:
    #     verbose_name = 'One News'
    #     verbose_name_plural = 'News'





class Contest(models.Model):

    сontest_title = models.CharField(max_length=100)
    сontest_date = models.DateTimeField()
    сontest_image = models.TextField()
    сontest_text = models.TextField()
    сontest_files = models.TextField()
    # @property
    # def сontest_files(self):
    #     list_id = [{i.file} for i in FeedFile.objects.filter(feed=self)]
    #     return list_id

class FeedFile(models.Model):
    file = models.FileField(upload_to="files/%Y/%m/%d")
    feed = models.ForeignKey(Contest, on_delete=models.CASCADE)


