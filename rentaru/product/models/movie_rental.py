from django.db import models
from .client import Client
from .movie import Movie

import uuid

class MovieRental(models.Model):
    client_id = models.ForeignKey(Client, default=uuid.uuid4, on_delete=models.CASCADE, db_column='client_id')
    movie_id = models.ForeignKey(Movie, default=uuid.uuid4, on_delete=models.CASCADE, db_column='movie_id')
    rented_at = models.DateField()
    payment_type = models.CharField(max_length=255)
    price = models.FloatField(default=0)