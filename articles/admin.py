from django.contrib import admin

from articles.models import Article, Tag
from core.admin import BaseAdmin


@admin.register(Tag)
class TagAdmin(BaseAdmin):
    list_display = 'display_id', 'name',
    exclude = 'display_id', 'slug'


@admin.register(Article)
class ArticleAdmin(BaseAdmin):
    exclude = 'display_id', 'slug'
    list_display = 'display_id', 'title', 'is_approved', 'created'
    list_filter = ("is_approved",)
    search_fields = ['title', 'content']
    filter_horizontal = 'related_topics',
