from django.urls import path
from . import views

app_name = "questions"

urlpatterns = [
    path("", views.QuestionsList.as_view()),
    path("<int:pk>", views.QuestionDetail.as_view()),
    path("create", views.CreateQuestion.as_view()),
]
