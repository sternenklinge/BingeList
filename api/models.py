from django.db import models

# Create your models here.
class Media(models.Model):
    tmdb_id = models.IntegerField()
    title = models.CharField(max_length=255)
    poster_path = models.CharField(max_length=255)
    overview = models.TextField()
    release_date = models.DateField()
    is_movie = models.BooleanField()

class Season(models.Model):
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    season_number = models.IntegerField()

class Episode(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    episode_number = models.IntegerField()
    name = models.CharField(max_length=255)

class Watchlist(models.Model):
    tmdb_id = models.IntegerField()
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=255)
    # status = models.CharField(max_length=255, choices=[("planed", "planed"), ("watching", "watching"), ("abandoned", "abandoned"), ("completed", "completed")])
