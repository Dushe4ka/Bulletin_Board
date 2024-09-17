from django.contrib import admin
from board.models import Advertisement, Feedback


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price", "description", "author", "created_at")


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "author", "ad", "created_at")
