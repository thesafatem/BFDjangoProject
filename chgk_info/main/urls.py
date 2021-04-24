from django.urls import path
from .views import *

urlpatterns = [
    path('cities/', cities_list),
    path('cities/<int:pk>/', CityDetailView.as_view()),
    path('teams/', teams_list),
    path('teams/<int:pk>/', TeamDetailView.as_view()),
    path('players/', PlayerListView.as_view()),
    path('players/<int:pk>/', PlayerDetailView.as_view()),
    path('tournaments/', TournamentBaseViewSet.as_view({'get': 'list'})),
    path('tournaments/<int:pk>/', TournamentBaseViewSet.as_view({'get': 'retrieve', 'delete': 'delete'})),
    path('synchrons/', SynchronousViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('synchrons/<int:pk>/', SynchronousViewSet.as_view({'get': 'retrieve', 'delete': 'delete'})),
    path('cups/', CupViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('cups/<int:pk>/', CupViewSet.as_view({'get': 'retrieve', 'delete': 'delete'}))
]