from rest_framework import serializers
from city.serializers import CityBaseSerializer
from .models import Team


class TeamBaseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)


class TeamSerializer(TeamBaseSerializer):
    id = serializers.IntegerField(read_only=True)
    city = CityBaseSerializer()


class TeamCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'