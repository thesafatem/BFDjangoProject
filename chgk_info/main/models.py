from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=255, null=False)
    rating = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)


class Player(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    rating = models.IntegerField()


class TournamentBaseModel(models.Model):
    name = models.CharField(max_length=255, null=False)
    number_of_questions = models.IntegerField()
    difficulty_level = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()

    # class Meta:
    #     abstract = True


class Synchronous(TournamentBaseModel):
    question_file = models.FileField()


class Cup(TournamentBaseModel):
    city = models.ForeignKey(City, on_delete=models.CASCADE)


class TournamentCompetitorsTeams(models.Model):
    tournament = models.ForeignKey(TournamentBaseModel, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    alias_name = models.CharField(max_length=255)


class TournamentCompetitorsPlayers(models.Model):
    tournament_team = models.ForeignKey(TournamentCompetitorsTeams, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)