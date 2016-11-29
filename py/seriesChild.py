from videoParent import Video

class Series(Video):
    """ Provides an abstraction to Serie objects - intended to be a child of Video """

    def __init__(self, serie_title, serie_storyline, poster_image, youtube_url_video, episode_length):
        Video.__init__(self, serie_title, poster_image, youtube_url_video, episode_length, serie_storyline)