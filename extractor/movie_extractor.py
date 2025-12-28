import http.client
import json
import os
from dotenv import load_dotenv

load_dotenv()  

def extract_movie_data():
    api_host = os.getenv("RAPIDAPI_HOST")
    api_key  = os.getenv("RAPIDAPI_KEY")
    endpoint = os.getenv("ENDPOINT")

    if not api_host or not api_key or not endpoint:
        raise EnvironmentError("❌ Missing required environment variables")

    conn = http.client.HTTPSConnection(api_host)

    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": api_host
    }

    conn.request("GET", endpoint, headers=headers)
    res = conn.getresponse()
    raw_data = res.read()

    payload = json.loads(raw_data.decode("utf-8"))

    extracted_movies = []

    for show in payload.get("shows", []):
        movie = {
            "movie_id": show.get("id"),
            "title": show.get("title"),
            "original_title": show.get("originalTitle"),
            "release_year": show.get("releaseYear"),
            "runtime_minutes": show.get("runtime"),
            "rating": show.get("rating"),
            "genres": [g["name"] for g in show.get("genres", [])],
            "available_on": [
                {
                    "platform": opt["service"]["name"],
                    "type": opt.get("type"),
                    "quality": opt.get("quality")
                }
                for opt in show.get("streamingOptions", {}).get("in", [])
            ]
        }
        extracted_movies.append(movie)

    return extracted_movies
