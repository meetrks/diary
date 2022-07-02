from django.contrib import admin

from core.admin import BaseAdmin
from storage.models import ImageCollection


@admin.register(ImageCollection)
class ImageCollectionAdmin(BaseAdmin):
    list_display = ('title', 'poster_url', 'created')
    list_filter = ('created',)
