from django.contrib import admin
from django.utils.html import mark_safe
from .models import Photo, Event

# Register your models here.
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Кастомная админка для фото"""

    list_display = (
        "__str__",
        "get_thumbnail",
    )

    def get_thumbnail(self, obj):
        return mark_safe(f'<img src="{obj.file.url}" width=50/>')

    get_thumbnail.short_description = "Preview"


class PhotoInline(admin.StackedInline):
    model = Photo


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """Админка новости"""

    inlines = [
        PhotoInline,
    ]

    fieldsets = (
        (
            "Event Info",
            {
                "fields": (
                    "title",
                    "short_description",
                    "text",
                ),
            },
        ),
    )

    list_display = [
        "id",
        "title",
        "short_description",
        "created",
        "text",
        "count_photos",
    ]

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photos"
