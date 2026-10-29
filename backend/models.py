from pydantic import BaseModel, Field

class Movie(BaseModel):
    id: int = Field(description="Id de la película de TMDB", gt=0)
    title: str = Field(description="Título de la película", min_length=1)
    overview: str = Field(description="Sinopsis")
    vote_average: float = Field(
        description="Puntuación media de la película", ge=0, le=10
    )
    poster_path: str | None = Field(
        default=None,
        description="Ruta del póster en TMDB"
    )