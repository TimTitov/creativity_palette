from django.contrib import admin
from .models import ClassImage, ClassNews


class NewsAdmin(admin.ModelAdmin):
    list_display = ('news_title', 'news_date', 'news_image', 'news_text')


class ImageAdmin(admin.ModelAdmin):
    list_display = ('image_url', 'image_date')


admin.site.register(ClassNews, NewsAdmin)

admin.site.register(ClassImage, ImageAdmin)
