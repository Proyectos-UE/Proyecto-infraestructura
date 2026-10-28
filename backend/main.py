from fastapi import FastAPI
from backend.routes import rutas

app = FastAPI(title="Movie Recommender API", description="API para consultar películas, realizar búsquedas y ofrecer recomendaciones personalizadas")

app.include_router(rutas)