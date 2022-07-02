from django.contrib import admin

from core.admin import BaseAdmin
from iam.models import User


@admin.register(User)
class UserAdmin(BaseAdmin):
    list_display = 'email', 'name', 'mobile_number'
    search_fields = 'name', 'email', 'mobile_number'
    fields = 'name', 'email', 'country_code', 'mobile_number', 'date_joined', 'groups', 'is_staff'
    readonly_fields = 'date_joined',
    filter_horizontal = 'groups',
