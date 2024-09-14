from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "first_name", "last_name", "phone", "role", "image")
    list_filter = ("first_name", "last_name", "email", "phone")
