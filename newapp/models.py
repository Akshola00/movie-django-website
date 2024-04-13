from django.db import models

# Create your models here.
class movies(models.Model):
    name = models.CharField(max_length=200)
    rating = models.FloatField()

    def __str__(self) -> str:
        return self.name
