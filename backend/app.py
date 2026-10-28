from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.templating import Jinja2Templates
from backend.app.tmdb.api import get_movies, search_movies
from backend.app.security import require_admin_key

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/health")
def health():
    """ Comprueba que nuestra API funciona"""
    return {"status": "ok"}

#para comprobar que nuestro end point esta protegido, se cambiará/modificará en un futuro para que la función tenga utilidad
@app.get("/admin/status",dependencies=[Depends(require_admin_key)])
def admin_status():
    return {
        "status": "ok",
        "service": "Movie Recommender"
    } 

@app.get("/")
def home(request: Request):
    """
    Home llamará a pelis famosas, listas y predicción y búsqueda
    """
    movies = get_movies() 
    if movies is None:
            raise HTTPException(
                status_code=503,
                detail="Movie service is currently unavailable"
            )
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "movies": movies["results"]
        }
    )

@app.get("/movies")
def movies():
    """
    Lista con todas las peliculas más busqueda
    """
    movies = get_movies() 
    if movies is None:
        raise HTTPException(
            status_code=503,
            detail="Movie service is currently unavailable")
    return movies["results"]

@app.get("/movies/search")
def search(request: Request, title: str):
    if not title:
        movies = get_movies()

    if movies is None:
        raise HTTPException(
            status_code=503,
            detail="Movie service is currently unavailable"
        )

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "movies": movies["results"]
        }
    )

