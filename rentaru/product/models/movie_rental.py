from django.db import models
from .client import Client
from .movie import Movie


class MovieRental(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE)
    rented_at = models.DateField()
    payment_type = models.CharField(max_length=255)
    price = models.FloatField(default=0)
