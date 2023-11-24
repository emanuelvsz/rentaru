from django.urls import path
from product.views import *

urlpatterns = [
    path('movies', MovieListAPIView.as_view(), name='movie_list'),
    path('movies/<uuid:movie_id>/delete', MovieDeleteAPIView.as_view(), name='delete_movie'),
    path('movies/<uuid:movie_id>', MovieByIDAPIView.as_view(), name="movie_by_id"),
    path('movies/<uuid:movie_id>/update', MovieUpdateAPIView.as_view(), name="movie_update"),
    path('client', ClientListAPIView.as_view(), name="client_list"),
    path('client/update', ClientDetailAPIView.as_view(), name="client_update")
]
