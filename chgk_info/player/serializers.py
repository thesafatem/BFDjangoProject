from rest_framework import serializers

from .models import Player
from team.serializers import TeamBaseSerializer
from city.serializers import CityBaseSerializer
# from tournament.serializers import TCPSerializer
import tournament.serializers


class DemoPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'rating']


class PlayerCreateSerializer(DemoPlayerSerializer):
    class Meta(DemoPlayerSerializer.Meta):
        fields = DemoPlayerSerializer.Meta.fields + ['city', 'team']


class PlayerNestedSerializer(PlayerCreateSerializer):
    team = TeamBaseSerializer()
    city = CityBaseSerializer()


class PlayerShowSerializer(PlayerNestedSerializer):
    tournaments = tournament.serializers.TCPSerializer(read_only=True, many=True)

    class Meta(PlayerNestedSerializer.Meta):
        fields = PlayerNestedSerializer.Meta.fields + ['tournaments']