from django.contrib import admin
from .models import Question

# Register your models here.
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Админка вопроса"""

    fieldsets = (
        (
            "Question",
            {
                "fields": (
                    "text",
                    "owner",
                ),
            },
        ),
        (
            "Answer",
            {
                "fields": ("answer",),
            },
        ),
        (
            "Additional Info",
            {
                "fields": (
                    "public",
                    "category",
                )
            },
        ),
    )

    raw_id_fields = ("owner",)

    list_display = (
        "id",
        "text",
        "owner",
        "created",
        "public",
        "category",
        "answer",
        "created_answer",
        "count_comments",
    )

    list_filter = (
        "public",
        "category",
    )

    search_fields = ("text",)

    def count_comments(self, obj):
        return obj.comments.count()

    count_comments.short_description = "Comments"
