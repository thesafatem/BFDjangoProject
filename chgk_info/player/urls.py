from django.urls import path
from .views import PlayerListView, PlayerDetailView

urlpatterns = [
    path('', PlayerListView.as_view()),
    path('<int:pk>/', PlayerDetailView.as_view())
]