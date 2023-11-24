from django.core.exceptions import ObjectDoesNotExist
from product.models import Movie

class MovieService:
    def get_movies(self):
        try:
            data = Movie.objects.all()
            return data
        except Exception as e:
            raise ValueError(f"Failed to delete movie with id {id}. Error: {str(e)}")
        
    def get_movie_by_id(self, id):
        try:
            movie = Movie.objects.get(id=id)
            return movie
        except ObjectDoesNotExist:
            raise ValueError(f"Movie with id {id} does not exist.")
        except Exception as e:
                raise ValueError(f"Failed to list movie with id {id}. Error: {str(e)}")
            
    def delete_movie_by_id(self, id):
        try:
            movie = Movie.objects.get(id=id)
            movie.delete()
        except ObjectDoesNotExist:
            raise ValueError(f"Movie with id {id} does not exist.")
        except Exception as e:
            raise ValueError(f"Failed to delete movie with id {id}. Error: {str(e)}")
        
    def update_movie(self, id, movie_data):
        try:
            movie = Movie.objects.get(id=id)
            for field in Movie._meta.get_fields():
                field_name = field.name
                if hasattr(movie_data, field_name):
                    new_value = getattr(movie_data, field_name)
                    if new_value is not None:
                        setattr(movie, field_name, new_value)
            movie.save()
            return movie
        except ObjectDoesNotExist:
            raise ValueError(f"Movie with id {id} does not exist.")
        except Exception as e:
            raise ValueError(f"Failed to update movie with id {id}. Error: {str(e)}")