from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response

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
    def get(self, request, pk):
        queryset = City.objects.all()
        city = get_object_or_404(queryset, pk=pk)
        serializer = CitySerializer(city)
        return Response(serializer.data)

    def delete(self, request, pk):
        queryset = City.objects.all()
        city = get_object_or_404(queryset, pk=pk)
        city.delete()
        return Response(status=204)