from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .models import ChgkUser
from .serializers import ChgkUserSerializer, ChgkUserRegistrationSerializer
from tournament.serializers import ApplicationSerializer, RegularSerializer
from tournament.models import Application, Regular
# Create your views here.


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


class ProfileViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request):
        app_queryset = Application.objects.select_related().filter(host=request.user.id)
        app_serializer = ApplicationSerializer(app_queryset, many=True)
        synchron_ids = []
        for x in app_serializer.data:
            synchron_ids.append(x['synchron'])
        sync_queryset = Regular.objects.filter(id__in = synchron_ids)
        sync_serializer = RegularSerializer(sync_queryset, many=True)
        user_queryset = ChgkUser.objects.get(id=request.user.id)
        user_serializer = ChgkUserSerializer(user_queryset)
        y = user_serializer.data
        y['files'] = [x['question_file'] for x in sync_serializer.data]
        return Response(y)