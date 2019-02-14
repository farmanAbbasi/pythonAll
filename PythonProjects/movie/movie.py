import webbrowser
class Movie:
    '''this class Movies gets movies for representation'''
    VALID_RATINGS=["G","PG","PG-13","R"]
    def __init__(self,name,story,image,trailer):
        self.title=name
        self.storyline=story
        self.poster_image_url=image
        self.trailer_youtube_url=trailer

    def show_trailer(self):
        webbrowser.open(self.movie_trailer)
        
