from django.urls import path
from .views import teams_list, TeamDetailView

urlpatterns = [
    path('', teams_list),
    path('<int:pk>/', TeamDetailView.as_view()),
]