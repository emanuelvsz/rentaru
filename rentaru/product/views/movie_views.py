from product.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT
from product.selectors import *


class MovieDeleteAPIView(APIView):
    permission_classes = []
    
    def delete(self, _, movie_id):
        id = delete_movie_by_id(movie_id)
        return Response(id, status=HTTP_204_NO_CONTENT)

class MovieListAPIView(APIView):
    permission_classes = []
    
    def get(self, _):
        movies = get_movies()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
