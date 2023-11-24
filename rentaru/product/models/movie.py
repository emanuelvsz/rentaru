from django.db import models
import uuid

class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.CharField()
    release_date = models.DateField()
    director = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    cover_image = models.URLField()
    trailer_url = models.URLField(null=True, blank=True)
    rental_price = models.FloatField(default=0)

    def __str__(self):
        return self.title
