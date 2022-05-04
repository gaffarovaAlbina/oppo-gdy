from xml.etree.ElementTree import Comment
from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from .models import Comment
from . import serializers

# Create your views here.
class CreateComment(generics.CreateAPIView):
    """Представление создания комментария"""

    queryset = Comment.objects.all()
    serializer_class = serializers.CreateCommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        id = self.request.user.id

        user = User.objects.get(pk=id)

        serializer.save(owner=user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(status=status.HTTP_201_CREATED, headers=headers)
