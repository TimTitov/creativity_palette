# Generated by Django 3.0.4 on 2020-03-24 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20200324_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filemodel',
            name='file_url',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='files'),
        ),
    ]
