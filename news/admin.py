from django.contrib import admin
from .models import News, ImageModel


class NewsAdmin(admin.ModelAdmin):
    list_display = ('news_title', 'news_date', 'news_image', 'news_text')


class ImageAdmin(admin.ModelAdmin):
    list_display = ('image_url', 'image_date')


admin.site.register(News, NewsAdmin)

admin.site.register(ImageModel, ImageAdmin)