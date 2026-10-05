from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.templating import Jinja2Templates
from tmdb.api import get_movies, search_movies
from security import require_admin_key

app = FastAPI()

templates = Jinja2Templates(directory="templates")

#para comprobar que nuestro end point esta protegido, se cambiará/modificará en un futuro para que la función tenga utilidad
@app.get("/admin/status",dependencies=[Depends(require_admin_key)])
def admin_status():
    return {
        "status": "ok",
        "service": "Movie Recommender"
    } 

@app.get("/")
def home(request: Request):
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

@app.get("/search")
def search(request: Request, title: str):
    if not title:
        return templates.TemplateResponse(
            request=request,
            name="index.html",
            context={
                "movies": get_movies()["results"]
            }
        )
    search_results = search_movies(title)
    if search_results is None:
        raise HTTPException(
            status_code=503,
            detail="Movie service is currently unavailable"
        )
    return templates.TemplateResponse(
        request=request,
        name="search.html",
        context={
            "movies": search_results["results"],
            "title": title
        }
    )

