from django.core.exceptions import ObjectDoesNotExist
from product.models import Movie

class MovieService:
    def get_movies(self):
        return Movie.objects.all()
    
    def delete_movie_by_id(self, id):
        try:
            movie = Movie.objects.get(id=id)
            movie.delete()
            return movie.id
        except ObjectDoesNotExist:
            raise ValueError(f"Movie with id {id} does not exist.")
        except Exception as e:
            raise ValueError(f"Failed to delete movie with id {id}. Error: {str(e)}")