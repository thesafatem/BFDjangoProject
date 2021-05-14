from rest_framework import serializers
from .models import Player
from team.serializers import TeamBaseSerializer
from city.serializers import CityBaseSerializer


class PlayerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


class PlayerSerializer(PlayerCreateSerializer):
    team = TeamBaseSerializer()
    city = CityBaseSerializer()