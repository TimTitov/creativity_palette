from django.contrib import admin
from .models import News, ImageModel, FileModel, Contest, FeedFile


class NewsAdmin(admin.ModelAdmin):
    list_display = ('news_title', 'news_date', 'news_image', 'news_text')


class ImageAdmin(admin.ModelAdmin):
    list_display = ('image_url', 'image_date')



class FileModelAdmin(admin.ModelAdmin):
    list_display = ('file_url', 'file_date')


admin.site.register(FileModel, FileModelAdmin)
admin.site.register(News, NewsAdmin)

admin.site.register(ImageModel, ImageAdmin)

class ContestAdmin(admin.ModelAdmin):
    list_display = ('сontest_title', 'сontest_date','сontest_image','сontest_text','сontest_files')


admin.site.register(Contest, ContestAdmin)

class FeedFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'feed')


admin.site.register(FeedFile, FeedFileAdmin)

# from django.contrib import admin
# from .models import Feed, FeedFile
#
# class FeedFileInline(admin.TabularInline):
#     model = FeedFile
#
#
# class FeedAdmin(admin.ModelAdmin):
#     inlines = [
#         FeedFileInline,
#     ]
#
# admin.site.register(Feed, FeedAdmin)