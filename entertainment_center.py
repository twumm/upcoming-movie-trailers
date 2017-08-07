'''This file makes a request to themoviedb.org's api and fetches the following
movie details:
title, storyline/overview, poster image url, youtube trailer url and the
release date
'''
import media
import fresh_tomatoes
import requests

# access the api and convert it to a json file
MOVIE_LIST = requests.get("https://api.themoviedb.org/3/movie/upcoming?" +
                          "api_key=03531cf9267cbb1ee25c65670346beca&page=1")
MOVIE_DATA = MOVIE_LIST.json()
MOVIE_TRAILER_BASE_URL = "https://api.themoviedb.org/3/movie/"
MOVIE_TRAILER_END_URL = "/videos?api_key=03531cf9267cbb1ee25c65670346beca"
POSTER_BASE_URL = "https://image.tmdb.org/t/p/w500"
YOUTUBE_TRAILER_BASE_URL = "https://www.youtube.com/watch?v="
MOVIES = []

for item in MOVIE_DATA["results"][:10]:
    # Loop through the response received from api.themoviedb.org and pick out
    # the title, overview and movie image
    movie_title = item["title"]
    movie_storyline = item["overview"][:200].encode('utf8') + "...read more"
    poster_image = POSTER_BASE_URL + item["poster_path"]
    release_date = item["release_date"]

    # Get the video feed for each movie item and assign the video URL to
    # trailer_youtube
    movie_id = str(item["id"])
    movie_trailer_list = requests.get(MOVIE_TRAILER_BASE_URL + movie_id +
                                      MOVIE_TRAILER_END_URL)
    movie_trailer_data = movie_trailer_list.json()
    trailer_youtube = YOUTUBE_TRAILER_BASE_URL \
        + movie_trailer_data["results"][0]["key"]

    # Create an instance of the Movie() class using the items
    movie_instance = media.Movie(movie_title, movie_storyline, poster_image,
                                 trailer_youtube, release_date)
    # Append the movies to the movies[] array
    MOVIES.append(movie_instance)

# The open_movies_page displays the movies in the browser
fresh_tomatoes.open_movies_page(MOVIES)
