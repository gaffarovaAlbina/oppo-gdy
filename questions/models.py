from datetime import datetime
from django.db import models
from core import models as core_models
from users.models import User


# Create your models here.
class Question(core_models.AbstractItem):
    """Модель вопроса"""

    HEALTH = "Здоровье"
    STUDY = "Обучение"
    FINANCE = "Финансы"
    DOCUMENTS = "Документы"
    OTHER = "Другое"
    CATEGORIES = (
        (HEALTH, "Здоровье"),
        (STUDY, "Обучение"),
        (FINANCE, "Финансы"),
        (DOCUMENTS, "Документы"),
        (OTHER, "Другое"),
    )

    owner = models.ForeignKey(
        User,
        related_name="questions",
        on_delete=models.CASCADE,
        null=True,
    )
    public = models.BooleanField(default=False)
    answer = models.TextField(null=True, blank=True, default="")
    created_answer = models.DateTimeField(null=True, blank=True)
    category = models.CharField(
        max_length=20, choices=CATEGORIES, null=True, blank=True
    )

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        try:
            question = Question.objects.get(pk=self.pk)
            if self.answer != question.answer:
                self.created_answer = datetime.now()
            super(Question, self).save(*args, **kwargs)  # Call the real save() method
        except Question.DoesNotExist:
            super(Question, self).save(*args, **kwargs)  # Call the real save() method
