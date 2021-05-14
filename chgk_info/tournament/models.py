from django.db import models
from .managers import TournamentBaseModelManager, TournamentCompetitorsTeamsManager
from city.models import City
from team.models import Team
from auth_.models import ChgkUser
from player.models import Player
# Create your models here.


class TournamentBaseModel(models.Model):
    name = models.CharField(max_length=255, null=False)
    number_of_questions = models.IntegerField()
    questions_per_tour = models.JSONField()
    difficulty_level = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()
    posted_by = models.ForeignKey(ChgkUser, on_delete=models.CASCADE, null=True)
    deleted = models.BooleanField(default=False)

    objects = TournamentBaseModelManager()

    class Meta:
        verbose_name = 'Соревнование'
        verbose_name_plural = 'Соревнования'

    def __str__(self):
        return self.name


class Regular(TournamentBaseModel):
    question_file = models.FileField(upload_to='media')

    class Meta:
        verbose_name = 'Синхрон'
        verbose_name_plural = 'Синхроны'


class Cup(TournamentBaseModel):
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Очник'
        verbose_name_plural = 'Очники'


class TournamentCompetitorsTeams(models.Model):
    tournament = models.ForeignKey(TournamentBaseModel, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    alias_name = models.CharField(max_length=255, null=True)
    results = models.JSONField(default=None)

    objects = TournamentCompetitorsTeamsManager()

    class Meta:
        verbose_name = 'Команда-участница'
        verbose_name_plural = 'Команды-участницы'

    def __str__(self):
        return self.tournament.__str__() + ' ' + self.team.__str__()


class TournamentCompetitorsPlayers(models.Model):
    tournament_team = models.ForeignKey(TournamentCompetitorsTeams, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Игрок-участник'
        verbose_name_plural = 'Игроки-участники'

    def __str__(self):
        return self.tournament_team.__str__() + ' ' + self.player.__str__()


class Application(models.Model):
    regular = models.ForeignKey(Regular, on_delete=models.CASCADE)
    representative = models.ForeignKey(ChgkUser, on_delete=models.SET_NULL, null=True, related_name='representative')
    host = models.ForeignKey(ChgkUser, on_delete=models.SET_NULL, null=True, related_name='host')
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.regular.__str__() + ' ' + self.representative.__str__() + ' ' + self.host.__str__()