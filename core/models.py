from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    """Общие поля с датой, временем"""

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class AbstractItem(TimeStampedModel):
    """Абстрактный объект"""

    text = models.TextField(default="")

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
