from django.contrib import admin
from .models import Administrator


class AdministratorAdmin(admin.ModelAdmin):
    list_display = ('login', 'password')


admin.site.register(Administrator, AdministratorAdmin)
