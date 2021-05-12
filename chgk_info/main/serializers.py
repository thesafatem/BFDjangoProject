from abc import ABC

from rest_framework import serializers
from .models import *


class CityBaseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)


class CitySerializer(CityBaseSerializer):
    id = serializers.IntegerField(read_only=True)


class TeamBaseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)


class TeamSerializer(TeamBaseSerializer):
    id = serializers.IntegerField(read_only=True)
    city = CityBaseSerializer()


class PlayerSerializer(serializers.ModelSerializer):
    team = TeamBaseSerializer()
    city = CityBaseSerializer()

    class Meta:
        model = Player
        fields = '__all__'

        ordering = ('firstname',)


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


class TournamentCompetitorsTeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentCompetitorsTeams
        fields = '__all__'


class TournamentBaseModelSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if data['difficulty_level'] < 1:
            raise serializers.ValidationError('Difficulty level is too low')
        if data['difficulty_level'] > 10:
            raise serializers.ValidationError('Difficulty is too high')
        if not data['difficulty_level'].is_integer() and not (data['difficulty_level'] + 0.5).is_integer():
            raise serializers.ValidationError('Difficulty is not of step 0.5')

        if data['end_date'] < data['start_date']:
            raise serializers.ValidationError('''End date can't exceed start date''')

        return data

    class Meta:
        model = TournamentBaseModel
        validators = []
        fields = '__all__'


class SynchronousSerializer(TournamentBaseModelSerializer):
    class Meta:
        model = Synchronous
        validators = []
        fields = '__all__'


class CupSerializer(TournamentBaseModelSerializer):
    class Meta:
        model = Cup
        validators = []
        fields = '__all__'


class TournamentCompetitorsPlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentCompetitorsPlayers
        fields = '__all__'


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

