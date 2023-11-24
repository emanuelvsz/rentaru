from product.services import *

def get_movies():
    return MovieService().get_movies()

def delete_movie_by_id(id): 
    return MovieService().delete_movie_by_id(id)

def get_movie_by_id(id):
    return MovieService().get_movie_by_id(id)

def update_movie(id, movie_data):
    return MovieService().update_movie(id, movie_data)