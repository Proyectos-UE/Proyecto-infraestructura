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
    url = "https://api.themoviedb.org/3/movie/popular"

    response = requests.get(url, headers=headers)

    return response.json()