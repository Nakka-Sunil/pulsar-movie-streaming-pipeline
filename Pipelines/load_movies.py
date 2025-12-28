from Movie_Streaming.extractor.movie_extractor import extract_movie_data


def run_pipeline(): 
    movies = extract_movie_data()
    #get_movies(movies)
    return movies
    