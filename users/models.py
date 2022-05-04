from turtle import position
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    """Кастомная модель пользователя"""

    REQUIRED_FIELDS = ()

    patronymic = models.CharField(max_length=150, null=True, blank=True)
    position = models.CharField(max_length=200, default="")
    avatar = models.ImageField(null=True, blank=True, upload_to="avatars")

    def get_full_name(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    def __str__(self):
        return f"{self.get_full_name()}"

    def save(self, *args, **kwargs):
        self.last_name = str.capitalize(self.last_name)
        self.first_name = str.capitalize(self.first_name)
        self.patronymic = str.capitalize(self.patronymic)
        self.position = str.capitalize(self.position)
        super().save(*args, **kwargs)
