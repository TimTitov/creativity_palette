from django.contrib import admin
from .models import ClassContest, ClassFile


class FilelAdmin(admin.ModelAdmin):
    list_display = ('file', 'feed')


admin.site.register(ClassFile, FilelAdmin)


class ContestAdmin(admin.ModelAdmin):
    list_display = ('сontest_title', 'сontest_date','сontest_image','сontest_text','сontest_files')


admin.site.register(ClassContest, ContestAdmin)

