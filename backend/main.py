from fastapi import FastAPI
from backend.routes import rutas

app = FastAPI()

app.include_router(rutas)