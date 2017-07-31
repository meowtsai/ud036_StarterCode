import webbrowser

class Movie():
    """A movie class contains movie titles, box art, poster images, and movie trailer URLs.
    Note this class should work well with fresh_tomatoes.py."""


    
    def __init__(self,title,movie_storyline,poster_image_url,trailer_youtube_url):
        self.title = title
        self.movie_storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url


