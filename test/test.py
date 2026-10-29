#Para comprobar que nuestros endpoints funcionan correctamente
import requests

url_base = "http://127.0.0.1:8000"

#Comprobar que la API responde
response = requests.get(f"{url_base}/movies")

#Función para manejo de errores
def checking_errors(url, params=None):
    try:
        response = requests.get(url, params=params, timeout=10)

        print("\nEndpoint:", response.url)
        print("Estado:", response.status_code)
        print("Content-Type:", response.headers.get("Content-Type"))

        response.raise_for_status()
        content_type = response.headers.get("Content-Type", "")

        if "application/json" in content_type:
            print("Respuesta JSON correcta")
            return response.json()

        elif "text/html" in content_type:
            print("Respuesta HTML correcta")
            return response.text

        else:
            print("Tipo de contenido no reconocido")
            return response.text

    except requests.Timeout:
        print("Error: tiempo de espera agotado")

    except requests.HTTPError as exc:
        status = exc.response.status_code

        if status == 401:
            print("401: Acceso no autorizado")

        elif status == 404:
            print("404: Recurso no encontrado")

        elif status == 422:
            print("422: Parámetros inválidos")

        elif status == 503:
            print("503: Servicio no disponible")

        else:
            print("Error HTTP:", status)

    except requests.exceptions.JSONDecodeError:
        print("Error: JSON inválido")

    except requests.RequestException as exc:
        print("Error de conexión:", exc)

    return None
    
print("Check de errores en endpoints")
checking_errors(f"{url_base}/health")
checking_errors(f"{url_base}/admin/status")
checking_errors(f"{url_base}/")
checking_errors(f"{url_base}/movies")
checking_errors(f"{url_base}/movies/search") #va a dar error porque no estamos buscando por título
checking_errors(f"{url_base}/login")