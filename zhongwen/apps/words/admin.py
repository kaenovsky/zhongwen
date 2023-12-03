from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import Word

class WordAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['en', 'es', 'zw', 'pinyin']

admin.site.register(Word, WordAdmin)