from django.db import models
from city.models import City
# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=255)
    rating = models.IntegerField(default=0)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'

    def __str__(self):
        return self.name