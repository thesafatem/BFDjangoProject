from rest_framework import serializers
from .models import City


class CityBaseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)


class CitySerializer(CityBaseSerializer):
    id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return City.objects.create(**validated_data)