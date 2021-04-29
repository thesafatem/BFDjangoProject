from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from .views import *

urlpatterns = [
    path('register/', ChgkUserViewSet.as_view({'post': 'create'})),
    path('login/', obtain_jwt_token),
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
    path('synchrons/<int:pk>/applications/', ApplicationViewSet.as_view({'post': 'create', 'get': 'list'})),
    path('cups/', CupViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('cups/<int:pk>/', CupViewSet.as_view({'get': 'retrieve', 'delete': 'delete'})),
    path('users/', ChgkUserViewSet.as_view({'get': 'list'})),
    path('users/<int:pk>/', ChgkUserViewSet.as_view({'get': 'retrieve'})),
    path('profile/', ProfileViewSet.as_view({'get': 'retrieve'}))
]