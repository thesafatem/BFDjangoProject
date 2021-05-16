from rest_framework import serializers
from .models import ChgkUser
from player.serializers import PlayerNestedSerializer


class ChgkUserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        if (data.get('first_name') is None or data.get('last_name') is None) and data.get('profile') is None:
            raise serializers.ValidationError('You should give either your name or profile')
        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        chgk_user = ChgkUser.objects.create_user(**validated_data)
        chgk_user.set_password(password)
        chgk_user.save()
        return chgk_user

    class Meta:
        model = ChgkUser
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'profile']
        validators = []


class ChgkUserSerializer(serializers.ModelSerializer):
    profile = PlayerNestedSerializer()

    class Meta:
        model = ChgkUser
        fields = ['id', 'first_name', 'last_name', 'email', 'profile']