from django.db import models
from account.models import *

# Create your models here.

class Movie(models.Model):
    movie_uid = models.CharField(default=uuid.uuid4,max_length=255)
    title = models.CharField(max_length=255)
    actors = models.ManyToManyField(Actor)
    genres = models.ManyToManyField(Genre)
    poster = models.ImageField(upload_to="media/movie/poster")
    banner_img = models.ImageField(upload_to="media/movie/banner")
    title_img = models.ImageField(upload_to="media/movie/title_img")
    is_adult = models.BooleanField(default=True)
    trailer = models.CharField(max_length=500)
    movie = models.CharField(max_length=500)
    released_date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=250,null=True)
    likes = models.IntegerField(default=0)
    
    

    def __str__(self) -> str:
        return f"{self.title}"



class Series(models.Model):
    title = models.CharField(max_length=255)
    no_of_season = models.IntegerField(default=0)
    is_adult = models.BooleanField(default=True)
    title_img = models.ImageField(upload_to="media/movie/title_img")
    genres = models.ManyToManyField(Genre)

    def __str__(self) -> str:
        return f"{self.title}"

class Season(models.Model):
    season_id = models.CharField(default=uuid.uuid4,max_length=255)
    series = models.ForeignKey(Series,on_delete=models.CASCADE,related_name="season")
    season_no = models.IntegerField(default=1)
    actors = models.ManyToManyField(Actor,related_name="season")
    poster = models.ImageField(upload_to="media/movie/poster")
    banner_img = models.ImageField(upload_to="media/movie/banner")
    trailer = models.CharField(max_length=500)
    released_date = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    description = models.CharField(max_length=250,null=True)

    def __str__(self) -> str:
        return f"{self.series} {self.season_no}"
    
    def save(self, *args, **kwargs):
        series = self.series
        no_of_season = series.no_of_season
        no_of_season += 1
        series.no_of_season = no_of_season
        series.save()
        return super().save(*args, **kwargs)

class Episode(models.Model):
    season = models.ForeignKey(Season,on_delete=models.CASCADE,related_name="episode")
    episode_no = models.IntegerField(default=1)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    thumbnail = models.CharField(max_length=350)
    episode = models.CharField(max_length=500)
    released_date = models.DateField(auto_now_add=True)



