from .views import get_first_mov,most_popular_genre,top_ten_movies,least_watched_movie
from .views import best_director_in_top100,get_post


from django.urls import path 
urlpatterns = [
     path('first/',get_first_mov),
     path('genre/',most_popular_genre),
     path('top/',top_ten_movies),
     path('least/',least_watched_movie),
     path('drctr/',best_director_in_top100),
     path('post/',get_post),
     


]