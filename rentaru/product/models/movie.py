from django.db import models
import uuid

class Movie(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.DurationField()

    def __str__(self):
        return self.name
