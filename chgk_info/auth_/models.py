from django.db import models
from django.contrib.auth.models import AbstractUser
from player.models import Player
from .managers import ChgkUserManager
# Create your models here.


class ChgkUser(AbstractUser):
    email = models.EmailField(blank=True, unique=True)
    username = models.CharField(max_length=255)  # ошибка нарушения уникальности -> override, чтобы убрать unique=True
    profile = models.OneToOneField(Player, on_delete=models.SET_NULL, null=True, related_name='chgk_user')

    objects = ChgkUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
