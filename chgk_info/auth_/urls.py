from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from .views import ChgkUserViewSet, ProfileViewSet

urlpatterns = [
    path('register/', ChgkUserViewSet.as_view({'post': 'create'})),
    path('login/', obtain_jwt_token),
    path('profile/', ProfileViewSet.as_view({'get': 'retrieve'}))
]