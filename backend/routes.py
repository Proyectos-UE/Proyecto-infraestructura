from fastapi import APIRouter, Request, HTTPException, Depends, Query
from fastapi.templating import Jinja2Templates
from backend.tmdb.api import get_movies, search_movies
from backend.security import require_admin_key
from backend.models import Movie
import requests

rutas = APIRouter()

templates = Jinja2Templates(directory="frontend/templates")

def movie_service_error():
    raise HTTPException(status_code=503, detail="Movie service is currently unavailable")

@rutas.get("/health", tags=["System"], description = "Comprueba que nuestra API funciona")
def health():
    """ Comprueba que nuestra API funciona"""
    return {"status": "ok"}

#para comprobar que nuestro end point esta protegido, se cambiará/modificará en un futuro para que la función tenga utilidad
@rutas.get("/admin/status", tags=["System"], dependencies=[Depends(require_admin_key)])
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

@rutas.get("/movies", tags=["Movies"], description="Consulta la API de TMDB y devuelve una lista de películas populares", response_model = list[Movie])
def movies():
    """
    Lista con todas las peliculas más busqueda
    """
    movies = get_movies() 
    if movies is None:
        movie_service_error()

    return movies["results"]

@rutas.get("/movies/search", tags=["Movies"], description="Hace una búsqueda de películas en base al título proporcionado", response_model = list[Movie])
def search(request: Request, title: str=Query(max_length = 50)):
    title = title.strip()
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

@rutas.api_route("/login", methods=["GET", "POST"]) #no esta puesta todavia como opción, escribir manualmente la ruta
async def manage_users(request: Request):
    """
    Recibe los datos del formulario de HTML, confirma que el usuario ya existe en la BD
    """
    user_email = None
    #simulación autenticación y autorizaión
    usuario = {
        "email": "test@gmail.com",
        "password": "1234",
        "status": "registered" #rol varia entre si el usuario esta registrado o no, si no lo está, se considera como visitante
    }
    if request.method == "POST":
        form = await request.form()
        user_email = form.get("email")
        password = form.get("password")
        print(user_email)

    if user_email == usuario["email"] and password == usuario["password"]:

        if usuario["status"] == "registered":
                mensaje = "Usuario autenticado y autorizado"
        else:
                mensaje = "No está registrado"

    else:
        mensaje = "Correo o contraseña incorrectos"

    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={"mensaje": mensaje}
    )    
