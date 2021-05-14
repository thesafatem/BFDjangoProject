from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Player
from .serializers import PlayerSerializer, PlayerCreateSerializer

# Create your views here.


class PlayerListView(APIView):
    def get(self, request):
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PlayerCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class PlayerDetailView(APIView):
    def get(self, request, pk):
        queryset = Player.objects.all()
        player = get_object_or_404(queryset, pk=pk)
        serializer = PlayerSerializer(player)
        return Response(serializer.data)

    def delete(self, request, pk):
        queryset = Player.objects.all()
        player = get_object_or_404(queryset, pk=pk)
        player.delete()
        return Response(status=204)