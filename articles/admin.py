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
    filter_horizontal = 'tags',

    change_form_template = 'admin/article_change_form.html'

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        instance = form.instance
        if not instance.creator:
            instance.creator = request.user
        if instance.is_approved and instance.publisher is None:
            instance.publisher = request.user
        instance.save()
