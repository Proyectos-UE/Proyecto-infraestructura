#test para ver los datos que nos devuelve la API
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from tmdb.api import get_movies

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