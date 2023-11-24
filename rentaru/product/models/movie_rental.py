from django.db import models

from .client import *
from .movie import *


class MovieRental(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_id')
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_id')
    rented_at = models.DateField()
    payment_type = models.CharField()
