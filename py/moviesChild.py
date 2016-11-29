from videoParent import Video
import webbrowser


class Movie(Video):
    """ Provides an abstraction to Movie objects - intended to be a child of Video """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_length):
        Video.__init__(self, movie_title, poster_image, trailer_youtube, movie_length)
        self.storyline = movie_storyline

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)