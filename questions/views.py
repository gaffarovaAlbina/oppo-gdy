from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework import status
from users.models import User
from .models import Question
from . import serializers

# Create your views here.
class QuestionsList(generics.ListAPIView):
    """Представление списка вопросов (только для чтения)"""

    queryset = Question.objects.all()
    serializer_class = serializers.QuestionsListSerializer

    def list(self, request, *args, **kwargs):

        id = request.user.id
        if id is not None:
            queryset = self.filter_queryset(self.get_queryset().filter(owner__pk=id))
        else:
            queryset = self.filter_queryset(
                self.get_queryset().filter(public=True).filter(answer__isnull=False)
            )

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class QuestionDetail(generics.RetrieveAPIView):
    """Представление списка вопросов (только для чтения)"""

    queryset = Question.objects.all()
    serializer_class = serializers.QuestionDetailSerializer


class CreateQuestion(generics.CreateAPIView):
    """Представление создания вопроса"""

    queryset = Question.objects.all()
    serializer_class = serializers.CreateQuestionSerializer
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
