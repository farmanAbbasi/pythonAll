import movie,fresh_tomatoes

def getMovies():
    
    bahubali=movie.Movie("Victorious","A quote of a warrior","1.bp.blogspot.com/-gmDYj6N_QJQ/UdwjbzKAjLI/AAAAAAAAVes/vpL6dO1Qu10/s1600/BitterOrBetter24.png","https://www.youtube.com/watch?v=t8ApMdi24LI&feature=player_embedded_uturn")
    #print(bahubali.movie_image)
    #bahubali.show_trailer()
    movies=[bahubali]
    #opens website
    #fresh_tomatoes.open_movies_page(movies)
    print(movie.Movie.VALID_RATINGS)
    print(movie.Movie.__doc__)
    print(movie.Movie.__name__)
    print(movie.Movie.__module__)
getMovies()


