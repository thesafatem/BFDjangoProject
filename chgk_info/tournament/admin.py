from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(TournamentBaseModel)
admin.site.register(Regular)
admin.site.register(Cup)
admin.site.register(TournamentCompetitorsTeams)
admin.site.register(TournamentCompetitorsPlayers)
admin.site.register(Application)
