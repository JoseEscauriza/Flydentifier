from django.contrib import admin
from apps.user.models import User
from django.contrib.auth.admin import UserAdmin


class CustomUser(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Fields', {"fields": ("bio",)}),
    )


admin.site.register(User, CustomUser)
