from django.contrib import admin
from comments.models import Comment
from questions.models import Question

# Register your models here.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Админка комментария"""

    fieldsets = (
        (
            "Comment",
            {
                "fields": (
                    "question",
                    "text",
                    "owner",
                )
            },
        ),
    )

    raw_id_fields = (
        "owner",
        "question",
    )

    list_display = (
        "id",
        "text",
        "owner",
        "created",
        "get_question",
        "get_category",
    )

    list_filter = ("question__category",)

    search_fields = ("text",)

    def get_question(self, obj):
        return obj.question.text

    def get_category(self, obj):
        return obj.question.category

    get_question.short_description = "Question"
    get_category.short_description = "Category"
