from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieListApiView(APIView):
    def get(self, request, *args, **kwargs):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
