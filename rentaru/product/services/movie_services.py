from django.core.exceptions import ObjectDoesNotExist
from product.models import Movie, MovieRental, Client

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
            
    def create_movie(self, movie_data):
        try:
            movie = Movie.objects.create(
                title=movie_data['title'],
                description=movie_data['description'],
                duration=movie_data['duration'],
                release_date=movie_data['release_date'],
                director=movie_data['director'],
                genre=movie_data['genre'],
                language=movie_data['language'],
                cover_image=movie_data['cover_image'],
                trailer_url=movie_data['trailer_url'],
                rental_price=movie_data['rental_price']
            )
            return movie
        except Exception as e:
            raise e
            
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
        
    def get_rented_movies(self):
        movies_rented = MovieRental.objects.all()
        rent_list = []
        for movie_rented in movies_rented:
            print("------=======================------")
            print(movie_rented.movie_id)
            print(movie_rented.client_id)            
            print("------=======================------")
            movie = Movie.objects.filter(id=movie_rented.movie).first()
            client = Client.objects.filter(id=movie_rented.client).first()
            rent_info = {
                'movie': {
                    'id': movie.id,
                    'title': movie.title
                },
                'client': {
                    'id': client.id,
                    'name': client.name
                },
                'rented_at': movie_rented.rented_at,
                'payment_type': movie_rented.payment_type,
                'price': movie_rented.price
            }
            rent_list.append(rent_info)
        return rent_list
