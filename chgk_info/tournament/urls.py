from django.urls import path
from .views import TournamentBaseViewSet, TournamentResultsViewSet, RegularViewSet, \
    ApplicationViewSet, CupViewSet, RegularUploadViewSet, CupUploadViewSet

urlpatterns = [
    path('', TournamentBaseViewSet.as_view({'get': 'list'})),
    path('<int:pk>/', TournamentBaseViewSet.as_view({'get': 'retrieve', 'delete': 'delete'})),
    path('<int:pk>/results/', TournamentResultsViewSet.as_view({'get': 'list'})),
    path('synchrons/', RegularViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('synchrons/<int:pk>/', RegularViewSet.as_view({'get': 'retrieve', 'delete': 'delete'})),
    path('synchrons/<int:pk>/applications/', ApplicationViewSet.as_view({'post': 'create', 'get': 'list'})),
    path('synchrons/<int:pk>/upload/', RegularUploadViewSet.as_view({'post': 'create'})),
    path('cups/', CupViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('cups/<int:pk>/', CupViewSet.as_view({'get': 'retrieve', 'delete': 'delete'})),
    path('cups/<int:pk>/upload/', CupUploadViewSet.as_view({'post': 'create'}))
]