from rest_framework import serializers
from .models import User


class UserNameSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source="get_full_name", read_only=True)

    class Meta:
        model = User
        fields = [
            "full_name",
        ]
