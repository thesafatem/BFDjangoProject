from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(City)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(TournamentBaseModel)
admin.site.register(Synchronous)
admin.site.register(Cup)
admin.site.register(TournamentCompetitorsTeams)
admin.site.register(TournamentCompetitorsPlayers)