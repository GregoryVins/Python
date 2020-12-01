from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    """
    Модель стандартного пользователя с добавлением поля никнейма.
    Данное поле не может быть пустым.
    """
    nickname = models.CharField(max_length=32, unique=True, blank=False)
