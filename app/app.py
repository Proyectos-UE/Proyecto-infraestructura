import os
from typing import Optional
from fastapi import FastAPI, HTTPException, Depends, Query, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, Field
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

SECRET_API_KEY = os.getenv("SECRET_API_KEY", "mi_token_secreto_123")

# Inicializar FastAPI (OpenAPI y Swagger UI se generan automáticamente)
app = FastAPI(
    title="API REST de Películas",
    description="API desarrollada con FastAPI que incluye validación, manejo de errores, autenticación y documentación OpenAPI.",
    version="1.0.0"
)

security = HTTPBearer()

# Esquema de validación con Pydantic
class FavoriteMovieRequest(BaseModel):
    movie_id: int = Field(..., gt=0, description="ID de la película (debe ser mayor a 0)")

# Sistema de Autenticación y Autorización
def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials != SECRET_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acceso no autorizado: Token inválido"
        )
    return credentials.credentials


# Endpoint 1: Obtener lista de películas con validación de parámetros query
@app.get("/api/movies", tags=["Películas"])
def get_movies(
    search: Optional[str] = Query(None, description="Término de búsqueda de película"),
    page: int = Query(1, ge=1, description="Número de página (debe ser >= 1)")
):
    movies = [
        {"id": 1, "title": "Inception", "year": 2010},
        {"id": 2, "title": "Interstellar", "year": 2014}
    ]

    if search:
        movies = [m for m in movies if search.lower() in m['title'].lower()]

    return {"page": page, "results": movies}


# Endpoint 2: Añadir película a favoritos (Requiere Autenticación y Validación Body)
@app.post("/api/favorites", status_code=status.HTTP_201_CREATED, tags=["Favoritos"])
def add_favorite(
    payload: FavoriteMovieRequest, 
    token: str = Depends(verify_token)
):
    return {
        "message": "Película añadida a favoritos con éxito",
        "movie_id": payload.movie_id
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)