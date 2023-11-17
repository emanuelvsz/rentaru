from product.services import *

def get_movies():
    return MovieService().get_movies()

def delete_movie_by_id(id): 
    return MovieService().delete_movie_by_id(id)
