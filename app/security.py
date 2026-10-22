#de momento no tenemos endpoints que proteger, pero en un futuro usaremos las funciones de este archivo para hacerlo 
import os
import secrets

from fastapi import HTTPException, Security
from fastapi.security import APIKeyHeader
from dotenv import load_dotenv

load_dotenv()

ADMIN_API_KEY = os.getenv("ADMIN_API_KEY")

if not ADMIN_API_KEY:
    raise RuntimeError("ADMIN_API_KEY is required")

key_header = APIKeyHeader(
    name="X-API-Key",
    auto_error=False
)

def require_admin_key(
    key: str | None = Security(key_header)
) -> None:

    if key is None or not secrets.compare_digest(
        key,
        ADMIN_API_KEY
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "APIKey"}
        )