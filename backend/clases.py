from pydantic import BaseModel, Field

class Movie(BaseModel):
    id: int = Field(description="Id de la película de TMDB")
    title: str = Field(description="Título de la película")
    overview: str = Field(description="Sinopsis")
    vote_average: float = Field(
        description="Puntuación media de la película"
    )
    poster_path: str | None = Field(
        default=None,
        description="Ruta del póster en TMDB"
    )