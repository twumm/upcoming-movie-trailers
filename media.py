'''Defines the class for the movies
'''
import webbrowser


class Movie():
    '''This program stores details on movies and shows their trailers'''
    # the __init__ function accepts 5 variables in order to instantiate a movie
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, release_date):
        '''Accepts 5 variables in order to instantiate a movie'''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = release_date

    # the show_trailer function opens the link to the movie which has been
    # clicked by the user
    def show_trailer(self):
        '''Opens the trailer of the movie file'''
        webbrowser.open(self.trailer_youtube_url)
