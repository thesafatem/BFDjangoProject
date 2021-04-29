from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse, Http404
from .models import *
from .serializers import *
# Create your views here.


@csrf_exempt
def cities_list(request):
    if request.method == 'GET':
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class CityDetailView(APIView):
    def get_object(self, pk):
        try:
            return City.objects.get(pk=pk)
        except City.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        city = self.get_object(pk)
        serializer = CitySerializer(city)
        return Response(serializer.data)

    def delete(self, request, pk):
        city = self.get_object(pk)
        city.delete()
        return Response(status=204)


@csrf_exempt
def teams_list(request):
    if request.method == 'GET':
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TeamSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class TeamDetailView(APIView):
    def get_object(self, pk):
        try:
            return Team.objects.get(pk=pk)
        except Team.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        team = self.get_object(pk)
        serializer = TeamSerializer(team)
        return Response(serializer.data)

    def delete(self, request, pk):
        team = self.get_object(pk)
        team.delete()
        return Response(status=204)


class PlayerListView(APIView):
    def get(self, request):
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class PlayerDetailView(APIView):
    def get_object(self, pk):
        try:
            return Player.objects.get(pk=pk)
        except Player.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        player = self.get_object(pk)
        serializer = PlayerSerializer(player)
        return Response(serializer.data)

    def delete(self, request, pk):
        player = self.get_object(pk)
        player.delete()
        return Response(status=204)


class ChgkUserViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = ChgkUserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def list(self, request):
        queryset = ChgkUser.objects.all()
        serializer = ChgkUserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        queryset = ChgkUser.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ChgkUserSerializer(user)
        return Response(serializer.data)


class TournamentBaseViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = TournamentBaseModel.objects.all()
        serializer = TournamentBaseModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        queryset = TournamentBaseModel.objects.all()
        tournament = get_object_or_404(queryset, pk=pk)
        serializer = TournamentBaseModelSerializer(tournament)
        return Response(serializer.data)

    def delete(self, request, pk):
        queryset = TournamentBaseModel.objects.all()
        tournament = get_object_or_404(queryset, pk=pk)
        tournament.delete()
        return Response(status=204)


class SynchronousViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Synchronous.objects.all()
        serializer = SynchronousSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        queryset = Synchronous.objects.all()
        synchron = get_object_or_404(queryset, pk=pk)
        serializer = TournamentBaseModelSerializer(synchron)
        return Response(serializer.data)

    def create(self, request):
        serializer = SynchronousSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        queryset = Synchronous.objects.all()
        synchron = get_object_or_404(queryset, pk=pk)
        synchron.delete()
        return Response(status=204)


class CupViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Cup.objects.all()
        serializer = CupSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        queryset = Cup.objects.all()
        cup = get_object_or_404(queryset, pk=pk)
        serializer = TournamentBaseModelSerializer(cup)
        return Response(serializer.data)

    def create(self, request):
        serializer = CupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        queryset = Cup.objects.all()
        cup = get_object_or_404(queryset, pk=pk)
        cup.delete()
        return Response(status=204)


class ApplicationViewSet(viewsets.ViewSet):
    permission_classes_by_action = {'create': [IsAuthenticated], 'list': [AllowAny]}

    def create(self, request, pk):
        queryset = Synchronous.objects.all()
        synchron = get_object_or_404(queryset, pk=pk)
        user = request.user
        request.data["representative"] = user.id
        request.data["synchron"] = pk
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def list(self, request, pk):
        queryset = Application.objects.filter(synchron=pk)
        serializer = ApplicationSerializer(queryset, many=True)
        return Response(serializer.data)


class ProfileViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request):
        app_queryset = Application.objects.select_related().filter(host=request.user.id)
        app_serializer = ApplicationSerializer(app_queryset, many=True)
        synchron_ids = []
        for x in app_serializer.data:
            synchron_ids.append(x['synchron'])
        sync_queryset = Synchronous.objects.filter(id__in = synchron_ids)
        sync_serializer = SynchronousSerializer(sync_queryset, many=True)
        user_queryset = ChgkUser.objects.get(id=request.user.id)
        user_serializer = ChgkUserSerializer(user_queryset)
        y = user_serializer.data
        y['files'] = [x['question_file'] for x in sync_serializer.data]
        return Response(y)
