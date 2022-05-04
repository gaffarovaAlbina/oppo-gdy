from rest_framework import serializers
from .models import Comment
from users.serializers import UserNameSerializer


class CommentsListSerializer(serializers.ModelSerializer):
    """Сериализатор для вывода списка комментариев."""

    owner = UserNameSerializer()

    class Meta:
        model = Comment
        fields = [
            "id",
            "owner",
            "text",
            "created",
        ]


class CreateCommentSerializer(serializers.ModelSerializer):
    """Сериализатор для создания комментария."""

    class Meta:
        model = Comment
        fields = [
            "text",
            "question",
        ]
