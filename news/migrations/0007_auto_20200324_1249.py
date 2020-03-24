# Generated by Django 3.0.4 on 2020-03-24 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20200323_1740'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_url', models.ImageField(blank=True, null=True, upload_to='', verbose_name='files')),
                ('file_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'File',
                'verbose_name_plural': 'Files',
            },
        ),
        migrations.DeleteModel(
            name='FileUpload',
        ),
    ]
