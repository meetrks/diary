from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    list_per_page = 20

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def get_fields(self, request, obj=None, **kwargs):
        fields = super().get_fields(request, obj, **kwargs)

        if not request.user.is_superuser:
            if 'is_approved' in fields:
                fields.remove('is_approved')
        else:
            if 'is_approved' in fields:
                fields += [fields.pop(0)]
        return fields


class ReadOnlyBaseAdmin(BaseAdmin):

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
