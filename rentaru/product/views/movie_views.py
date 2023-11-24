from product.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import *
from product.selectors import *


class MovieDeleteAPIView(APIView):
    permission_classes = []
    
    def delete(self, _, movie_id):
        delete_movie_by_id(movie_id)
        return Response(status=HTTP_204_NO_CONTENT)

class MovieListAPIView(APIView):
    permission_classes = []
    
    def get(self, _):
        movies = get_movies()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
class MovieByIDAPIView(APIView):
    permission_classes = []
    
    def get(self, _, movie_id):
        movie = get_movie_by_id(movie_id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
class MovieUpdateAPIView(APIView):
    permission_classes = []
    
    def patch(self, request, movie_id):
        movie_instance = get_movie_by_id(movie_id)
        movie_data = MovieSerializer(instance=movie_instance, data=request.data, partial=True)
        update_movie(movie_id, movie_data)
        return Response(status=HTTP_204_NO_CONTENT)