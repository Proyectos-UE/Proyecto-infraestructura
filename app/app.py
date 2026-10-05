#test para ver los datos que nos devuelve la API
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from tmdb.api import get_movies, search_movies

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):

    movies = get_movies()

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

    return templates.TemplateResponse(
        request=request,
        name="search.html",
        context={
            "movies": search_results["results"],
            "title": title
        }
    )

