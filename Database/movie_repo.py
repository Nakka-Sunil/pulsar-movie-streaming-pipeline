from .db_config import db_connection
import json
def get_movies(movie: dict):
    connection = db_connection()

    insert_query = """
    INSERT INTO MOVIE_SCHEMA.MOVIES
    (movie_id, title, original_title, release_year,
     runtime_minutes, rating, genres, available_on)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    """
    cursor = connection.cursor()
    print('Extraction Started...!')  
    cursor.execute(
            insert_query,
            (
                movie['movie_id'],
                movie['title'],
                movie['original_title'],
                movie['release_year'],
                movie['runtime_minutes'],
                movie['rating'],
                ",".join(movie['genres']),
                json.dumps(movie['available_on'])

                
            )
        )

    connection.commit()
    cursor.close()
    connection.close()
