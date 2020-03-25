from django.db import models


class ClassGallery(models.Model):
    gallery_title = models.CharField(max_length=100, blank=True, null=True)
    gallery_image = models.TextField(blank=True, null=True)
    gallery_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Gallery image'
        verbose_name_plural = 'Gallery images'

