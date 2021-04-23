from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=255, null=False)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=255, null=False)
    rating = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'

    def __str__(self):
        return self.name


class Player(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    rating = models.IntegerField()

    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'

    def __str__(self):
        return self.firstname + ' ' + self.lastname


class TournamentBaseModel(models.Model):
    name = models.CharField(max_length=255, null=False)
    number_of_questions = models.IntegerField()
    difficulty_level = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        verbose_name = 'Соревнование'
        verbose_name_plural = 'Соревнования'

    def __str__(self):
        return self.name


class Synchronous(TournamentBaseModel):
    question_file = models.FileField()

    class Meta:
        verbose_name = 'Синхрон'
        verbose_name_plural = 'Синхроны'


class Cup(TournamentBaseModel):
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Очник'
        verbose_name_plural = 'Очники'


class TournamentCompetitorsTeams(models.Model):
    tournament = models.ForeignKey(TournamentBaseModel, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    alias_name = models.CharField(max_length=255)

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