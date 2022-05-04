from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import mark_safe
from users.models import User


# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Кастомная админка для пользователей"""

    fieldsets = (
        (
            "User Info",
            {
                "fields": (
                    "username",
                    "password",
                    "email",
                ),
            },
        ),
        (
            "Personal Info",
            {
                "fields": (
                    "last_name",
                    "first_name",
                    "patronymic",
                    "position",
                    "avatar",
                )
            },
        ),
        (
            "Permissions",
            {
                "classes": ("collapse",),
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            "Important dates",
            {
                "classes": ("collapse",),
                "fields": (
                    "last_login",
                    "date_joined",
                ),
            },
        ),
    )

    add_fieldsets = (
        (
            "User Info",
            {
                "fields": (
                    "username",
                    "password",
                    "email",
                ),
            },
        ),
        (
            "Personal Info",
            {
                "fields": (
                    "last_name",
                    "first_name",
                    "patronymic",
                    "position",
                    "avatar",
                )
            },
        ),
        (
            "Permissions",
            {
                "classes": ("collapse",),
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )

    list_display = (
        "id",
        "get_thumbnail",
        "username",
        "last_name",
        "first_name",
        "patronymic",
        "position",
        "count_questions",
    )

    search_fields = (
        "=last_name",
        "=first_name",
        "=patronymic",
    )

    list_filter = ()

    def count_questions(self, obj):
        return obj.questions.count()

    count_questions.short_description = "Questions"

    def get_thumbnail(self, obj):
        return mark_safe(f'<img src="{obj.avatar.url}" width=50/>')

    get_thumbnail.short_description = "Avatar"
