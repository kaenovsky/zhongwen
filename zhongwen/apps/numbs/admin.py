from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import Numb

class NumbAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['num', 'zw', 'pinyin']

admin.site.register(Numb, NumbAdmin)