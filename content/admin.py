from django.contrib import admin
from .models import *
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display=["title","movie_uid","poster","banner_img","title_img","is_adult","trailer","movie","released_date","likes"]
admin.site.register(Movie,MovieAdmin)

class SeriesAdmin(admin.ModelAdmin):
    list_display=["title","no_of_season","is_adult","title_img"]
admin.site.register(Series,SeriesAdmin)

class SeasonAdmin(admin.ModelAdmin):
    list_display=["series","season_no","poster","banner_img","trailer","released_date","likes"]
admin.site.register(Season,SeasonAdmin)

class EpisodeAdmin(admin.ModelAdmin):
    list_display=["season","episode_no","name","description","thumbnail","episode","released_date"]
admin.site.register(Episode,EpisodeAdmin)