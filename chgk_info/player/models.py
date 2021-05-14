from django.db import models
from city.models import City
from team.models import Team
# Create your models here.


class Player(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return self.first_name + ' ' + self.last_name