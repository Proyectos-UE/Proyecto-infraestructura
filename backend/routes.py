from fastapi import APIRouter, Request, HTTPException, Depends
from fastapi.templating import Jinja2Templates
from backend.tmdb.api import get_movies, search_movies
from backend.security import require_admin_key

rutas = APIRouter()

templates = Jinja2Templates(directory="frontend/templates")

def movie_service_error():
    raise HTTPException(status_code=503, detail="Movie service is currently unavailable")

@rutas.get("/health")
def health():
    """ Comprueba que nuestra API funciona"""
    return {"status": "ok"}

#para comprobar que nuestro end point esta protegido, se cambiará/modificará en un futuro para que la función tenga utilidad
@rutas.get("/admin/status",dependencies=[Depends(require_admin_key)])
def admin_status():
    return {
        "status": "ok",
        "service": "Movie Recommender"
    } 

@rutas.get("/")
def home(request: Request):
    """
    Home con get movies y search movies
    """
    movies = get_movies()
    if movies is None:
        movie_service_error()
    
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={"movies": movies["results"]}
    )

@rutas.get("/movies")
def movies():
    """
    Lista con todas las peliculas más busqueda
    """
    movies = get_movies() 
    if movies is None:
        movie_service_error()

    return movies["results"]

@rutas.get("/movies/search")
def search(request: Request, title: str=""):

    result_search = search_movies(title)

    if result_search is None:
        movie_service_error()

    return templates.TemplateResponse(
        request=request,
        name="search.html",
        context={
            "movies": result_search["results"],
            "title": title
        }
    )

