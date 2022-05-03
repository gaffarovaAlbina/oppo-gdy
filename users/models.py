from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    """Кастомная модель пользователя"""

    REQUIRED_FIELDS = ()

    avatar = models.ImageField(null=True, blank=True, upload_to="avatars")
