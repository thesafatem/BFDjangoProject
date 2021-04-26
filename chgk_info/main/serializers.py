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


class ChgkUserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = ChgkUser
        fields = ['first_name', 'last_name', 'email', 'password', 'profile']

    def create(self, validated_data):
        password = validated_data.pop('password')
        chgk_user = ChgkUser.objects.create_user(**validated_data)
        chgk_user.set_password(password)
        chgk_user.save()
        return chgk_user


class ChgkUserSerializer(serializers.ModelSerializer):
    profile = PlayerSerializer()

    class Meta:
        model = ChgkUser
        fields = ['id', 'first_name', 'last_name', 'email', 'profile']


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


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

