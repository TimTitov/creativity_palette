from django.db import models


class ClassNews(models.Model):
    news_title = models.CharField(max_length=100)
    news_date = models.DateTimeField()
    news_image = models.TextField(blank=True, null=True)
    news_text = models.TextField()

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'


class ClassImage(models.Model):
    image_url = models.ImageField(verbose_name='images', upload_to='images', blank=True, null=True)
    image_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
