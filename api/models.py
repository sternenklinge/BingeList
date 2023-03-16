from django.db import models

# Create your models here.
class Watchlist(models.Model):
    movie_id = models.IntegerField()
#   overview = models.TextField()

