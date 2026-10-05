import os
import requests
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TMDB_API_TOKEN")

headers = {
    "Authorization": f"Bearer {token}",
    "accept": "application/json"
}


def get_movies():
    """
    Devuelve todas las pelis
    """
    url = "https://api.themoviedb.org/3/movie/popular"
    response = requests.get(url, headers=headers)

    return response.json()

def search_movies(title):
    """
    Sirve para que el usuario pueda buscar una película
    """
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        "query": title,
        "language": "es-ES"
    }

    response = requests.get(
        url,
        headers=headers,
        params=params
    )

    return response.json()
