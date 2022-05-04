from django.db import models
from core import models as core_models

# Create your models here.
class Event(core_models.AbstractItem):
    """Модель новости"""

    title = models.CharField(max_length=500, default="")
    short_description = models.TextField()

    def __str__(self):
        return self.title


class Photo(models.Model):
    """Модель фото"""

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="events_photos")
    event = models.ForeignKey(Event, related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
