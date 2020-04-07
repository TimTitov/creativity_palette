from django.db import models

# Create your models here.


class Administrator(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Admin'