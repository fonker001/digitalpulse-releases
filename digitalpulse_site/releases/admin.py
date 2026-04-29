# releases/admin.py
from django.contrib import admin
from .models import Release, Screenshot

class ScreenshotInline(admin.TabularInline):
    model = Screenshot
    extra = 1

@admin.register(Release)
class ReleaseAdmin(admin.ModelAdmin):
    list_display = ('version', 'is_latest', 'download_count')
    inlines = [ScreenshotInline]