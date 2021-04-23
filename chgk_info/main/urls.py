from django.urls import path
from .views import *

urlpatterns = [
    path('cities/', cities_list),
    path('cities/<int:pk>/', CityDetailView.as_view()),
    path('teams/', teams_list),
    path('teams/<int:pk>/', TeamDetailView.as_view()),
    path('players/', PlayerListView.as_view()),
    path('players/<int:pk>/', PlayerDetailView.as_view())
]