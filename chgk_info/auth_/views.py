from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .models import ChgkUser
from .serializers import ChgkUserSerializer, ChgkUserRegistrationSerializer
from tournament.serializers import ApplicationSerializer, RegularSerializer
from tournament.models import Application, Regular

import logging
logger = logging.getLogger('auth_')
# Create your views here.


class ChgkUserViewSet(viewsets.ViewSet):
    permission_classes_by_action = {'delete': [IsAuthenticated]}

    def create(self, request):
        serializer = ChgkUserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f'User (id = {serializer.data["id"]}, email = {serializer.data["email"]}) created')
            return Response(serializer.data)
        logger.info(serializer.errors)
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

    def delete(self, request):
        user = request.user
        id = user.id
        user.delete()
        logger.info(f'User (id = {id}) deleted')
        return Response(status=204)