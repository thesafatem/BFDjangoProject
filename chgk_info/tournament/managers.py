from django.db import models


class TournamentBaseModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class TournamentCompetitorsTeamsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by("-results__total")