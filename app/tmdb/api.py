import os
import requests
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TMDB_API_TOKEN")
print("Token cargado:", token is not None)

headers = {
    "Authorization": f"Bearer {token}",
    "accept": "application/json"
}

def hacer_request(url, params = None):
    try:
        response = requests.get(url, headers=headers,params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.Timeout:
        print("Request timed out")
        return None
    except requests.HTTPError as exc:
        print("HTTP error:", exc.response.status_code)
        return None
    except requests.exceptions.JSONDecodeError:
        print("The response is not valid JSON")
        return None
    except requests.RequestException:
        print("Connection error")
        return None

        
def get_movies():
    """
    Devuelve todas las pelis
    """
    url = "https://api.themoviedb.org/3/movie/popular"

    return hacer_request(url)

def search_movies(title):
    """
    Sirve para que el usuario pueda buscar una película
    """
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        "query": title,
        "language": "es-ES"
    }

    return hacer_request(url, params)
