class Video():
    """ Provides an abstraction to Video programs objects - intended to be a Father Class """
    def __init__(self, title, poster_image, youtube_trailer, duration_length, media_storyline):
        self.title = title
        self.trailer_youtube_url = youtube_trailer
        self.poster_image_url = poster_image
        self.length = duration_length
        self.storyline = media_storyline