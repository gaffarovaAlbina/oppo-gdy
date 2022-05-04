from rest_framework import serializers
from .models import Question
from comments.serializers import CommentsListSerializer
from users.serializers import UserNameSerializer


class QuestionsListSerializer(serializers.ModelSerializer):
    """Сериализатор для вывода списка комментариев."""

    class Meta:
        model = Question
        fields = [
            "id",
            "text",
            "created",
        ]


class QuestionDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для вывода деталей комментария."""

    comments = CommentsListSerializer(many=True)
    owner = UserNameSerializer()

    class Meta:
        model = Question
        fields = [
            "id",
            "text",
            "owner",
            "created",
            "category",
            "answer",
            "created_answer",
            "comments",
        ]
        depth = 1


class CreateQuestionSerializer(serializers.ModelSerializer):
    """Сериализатор для создания вопроса."""

    class Meta:
        model = Question
        fields = [
            "text",
            "category",
        ]
