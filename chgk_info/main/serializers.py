from rest_framework import serializers
from .models import *


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


class TournamentBaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentBaseModel
        fields = '__all__'


class SynchronousSerializer(serializers.ModelSerializer):
    class Meta:
        model = Synchronous
        fields = '__all__'


class CupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cup
        fields = '__all__'


class TournamentCompetitorsTeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentCompetitorsTeams
        fields = '__all__'


class TournamentCompetitorsPlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentCompetitorsPlayers
        fields = '__all__'