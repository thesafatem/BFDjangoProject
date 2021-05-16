from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Player
from .serializers import PlayerNestedSerializer, PlayerCreateSerializer, PlayerShowSerializer

import logging
logger = logging.getLogger('player')
# Create your views here.


class PlayerListView(APIView):
    def get(self, request):
        players = Player.objects.all()
        serializer = PlayerNestedSerializer(players, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PlayerCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f'Player (id = {serializer.data["id"]}) created')
            return Response(serializer.data)
        logger.info(serializer.errors)
        return Response(serializer.errors, status=400)


class PlayerDetailView(APIView):
    def get(self, request, pk):
        queryset = Player.objects.all()
        player = get_object_or_404(queryset, pk=pk)
        serializer = PlayerShowSerializer(player)
        return Response(serializer.data)

    def delete(self, request, pk):
        queryset = Player.objects.all()
        player = get_object_or_404(queryset, pk=pk)
        id = player.id
        player.delete()
        logger.info(f'Player (id = {id}) deleted')
        return Response(status=204)