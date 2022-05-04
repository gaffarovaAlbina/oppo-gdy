from django.urls import path
from . import views

app_name = "comments"

urlpatterns = [
    path("create", views.CreateComment.as_view()),
]
