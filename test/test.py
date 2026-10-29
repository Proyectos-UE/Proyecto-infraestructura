#Para comprobar que nuestros endpoints funcionan correctamente
import requests

url = "http://127.0.0.1:8000"

#Comprobar que la API responde
response = requests.get(f"{url}/movies", timeout=10)

print("Estado:", response.status_code)
print("Content-Type:", response.headers.get("Content-Type"))
#Si funciona, que extraiga campos de ejemplo de 3 pelis
if response.status_code == 200:
    movies = response.json()

    if movies:
        print("Título:", movies[0]["title"])
        print("Puntuación media:", movies[0]["vote_average"])
    else:
        print("No se encontraron películas")


#Probar cuando el endpoint no existe
response = requests.get(f"{url}/movies/random", timeout=10)

print("\nRecurso inexistente:")
print("Estado:", response.status_code)

if response.status_code == 404:
    print("Error 404 controlado correctamente")
else:
    print("Respuesta inesperada:", response.status_code)

#Ejemplo de búsqueda
response = requests.get(
    f"{url}/movies/search",
    params={"title": "Avatar"},
    timeout=10
)

print("\nBúsqueda de Avatar:")
print("Estado:", response.status_code)

if response.status_code == 200:
    print("Búsqueda realizada correctamente")
else:
    print("Error:", response.text)