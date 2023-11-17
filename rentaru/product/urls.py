from django.urls import path
from product.views import MovieListAPIView, MovieDeleteAPIView

urlpatterns = [
    path('movies', MovieListAPIView.as_view(), name='movie_list'),
    path('movies/<uuid:movie_id>/', MovieDeleteAPIView.as_view(), name='delete_movie'),
]
