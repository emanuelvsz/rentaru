from django.urls import path
from product.views import *

urlpatterns = [
    path('movies', MovieListAPIView.as_view(), name='movie_list'),
    path('movies/create', MovieCreateAPIView.as_view(), name="client_update"),
    path('movies/<uuid:movie_id>', MovieByIDAPIView.as_view(), name="movie_by_id"),
    path('movies/<uuid:movie_id>/update', MovieUpdateAPIView.as_view(), name="movie_update"),
    path('movies/<uuid:movie_id>/delete', MovieDeleteAPIView.as_view(), name='delete_movie'),
    path('movies/rented', MovieRentedAPIView.as_view(), name="rented_movies"),
    path('client', ClientListAPIView.as_view(), name="client_list"),
    path('client/create', ClientCreateAPIView.as_view(), name="client_update"),
    path('client/<uuid:client_id>', ClientByIDAPIView.as_view(), name="client_by_id"),
    path('client/<uuid:client_id>/update', ClientUpdateAPIView.as_view(), name="client_update"),
    path('client/<uuid:client_id>/delete', ClientDeleteAPIView.as_view(), name="client_update"),
    path('client/rent', ClientRentMovieAPIView.as_view(), name="client_update"),
]
