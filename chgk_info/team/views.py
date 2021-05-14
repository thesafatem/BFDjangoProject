from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Team
from .serializers import TeamCreateSerializer, TeamSerializer

import logging
logger = logging.getLogger('team')
# Create your views here.


@csrf_exempt
def teams_list(request):
    if request.method == 'GET':
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TeamCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f'Team (id = {serializer.data["id"]}, name = {serializer.data["name"]}) created')
            return JsonResponse(serializer.data, status=201)
        logger.info(serializer.errors)
        return JsonResponse(serializer.errors, status=400)


class TeamDetailView(APIView):
    def get(self, request, pk):
        queryset = Team.objects.all()
        team = get_object_or_404(queryset, pk=pk)
        serializer = TeamSerializer(team)
        return Response(serializer.data)

    def delete(self, request, pk):
        queryset = Team.objects.all()
        team = get_object_or_404(queryset, pk=pk)
        id = team.id
        name = team.name
        team.delete()
        logger.info(f'Team (id = {id}, name = {name}) deleted')
        return Response(status=204)