from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    # Extend the default fieldsets to include your custom fields
    fieldsets = DjangoUserAdmin.fieldsets + (
        ("Profile", {"fields": ("bio", "profile_picture", "followers")}),
    )

    
    add_fieldsets = DjangoUserAdmin.add_fieldsets + (
        ("Profile", {"fields": ("bio", "profile_picture")}),  # exclude followers at creation
    )

    list_display = ("id", "username", "email", "is_staff", "is_active")

    search_fields = ("username", "email")

    list_filter = ("is_staff", "is_active", "is_superuser")

    # To avoid clutter, followers is shown as a filterable M2M field
    filter_horizontal = ("followers",)
