from django.urls import path
from .views import MovieListCreateView, MovieListApiView

urlpatterns = [
    path('movies/', MovieListApiView.as_view(), name='movie-list'),
]
