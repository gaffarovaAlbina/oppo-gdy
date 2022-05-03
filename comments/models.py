from django.db import models
from core import models as core_models
from users.models import User
from questions.models import Question

# Create your models here.
class Comment(core_models.TimeStampedModel):
    """Модель комментария"""

    body = models.TextField(null=False, blank=False)
    owner = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    question = models.ForeignKey(
        Question, related_name="comments", on_delete=models.CASCADE
    )
