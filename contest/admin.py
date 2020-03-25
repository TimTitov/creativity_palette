from django.contrib import admin
from .models import ClassContest, ClassFile


class FileAdmin(admin.ModelAdmin):
    list_display = ('file', 'feed')


admin.site.register(ClassFile, FileAdmin)


class ContestAdmin(admin.ModelAdmin):
    list_display = ('contest_title', 'contest_date', 'contest_image', 'contest_text', 'contest_files')


admin.site.register(ClassContest, ContestAdmin)

