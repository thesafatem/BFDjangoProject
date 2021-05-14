from django.urls import path
from .views import cities_list, CityDetailView

urlpatterns = [
    path('', cities_list),
    path('<int:pk>/', CityDetailView.as_view())
]