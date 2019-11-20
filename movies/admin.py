from django.contrib import admin
from .models import Movie, Review, Genre

# Register your models here.
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'audience', 'poster_url', 'description',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content', 'score', 'user_id', 'movie_id',)
