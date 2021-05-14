from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import City
from .serializers import CitySerializer

import logging
logger = logging.getLogger('city')

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
            logger.info(f'City (id = {serializer.data["id"]}) created')
            return JsonResponse(serializer.data, status=201)
        logger.info(serializer.errors)
        return JsonResponse(serializer.errors, status=400)


class CityDetailView(APIView):
    def get(self, request, pk):
        queryset = City.objects.all()
        city = get_object_or_404(queryset, pk=pk)
        serializer = CitySerializer(city)
        return Response(serializer.data)

    def delete(self, request, pk):
        queryset = City.objects.all()
        city = get_object_or_404(queryset, pk=pk)
        id = city.id
        city.delete()
        logger.info(f'City (id = {id}) deleted')
        return Response(status=204)