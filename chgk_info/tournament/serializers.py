from rest_framework import serializers
from .models import TournamentBaseModel, Regular, Cup, TournamentCompetitorsPlayers, \
    TournamentCompetitorsTeams, Application
from team.serializers import TeamBaseSerializer


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
        exclude = ['deleted']


class RegularSerializer(TournamentBaseModelSerializer):

    class Meta:
        model = Regular
        validators = []
        exclude = ['deleted']


class CupSerializer(TournamentBaseModelSerializer):
    class Meta:
        model = Cup
        validators = []
        exclude = ['deleted']


class TournamentCompetitorsPlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentCompetitorsPlayers
        fields = '__all__'


class TournamentCompetitorsTeamsSerializer(serializers.ModelSerializer):
    team = TeamBaseSerializer()

    class Meta:
        model = TournamentCompetitorsTeams
        exclude = ['id']


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'