from rest_framework import serializers
from .models import Event, Photo


class PhotosListSerializer(serializers.ModelSerializer):
    """Сериализатор для вывода списка фото."""

    class Meta:
        model = Photo
        fields = [
            "id",
            "caption",
            "file",
        ]


class EventsListSerializer(serializers.ModelSerializer):
    """Сериализатор для вывода списка новостей."""

    photos = PhotosListSerializer(many=True)

    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "short_description",
            "text",
            "created",
            "photos",
        ]
        depth = 1
