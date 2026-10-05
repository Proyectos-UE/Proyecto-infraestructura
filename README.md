🎬 Sistema de Recomendación de Películas

Sistema web de recomendación de películas que genera sugerencias personalizadas a partir de las preferencias del usuario. El proyecto combina una aplicación web desarrollada con Python y HTML con técnicas de aprendizaje no supervisado y datos obtenidos de The Movie Database (TMDB).

📌 Descripción

El objetivo de este proyecto es desarrollar una plataforma capaz de recomendar películas adaptándose a los gustos de cada usuario.

La aplicación permitirá al usuario indicar sus preferencias de diferentes formas, por ejemplo:

🎯 Seleccionando características o preferencias cinematográficas.

⭐ Indicando una película que le haya gustado.

🎬 Introduciendo una lista de películas que le hayan gustado.

🔎 Obteniendo recomendaciones basadas en las películas seleccionadas.

A partir de esta información, el sistema analizará las características de las películas y buscará otras similares que puedan resultar interesantes para el usuario.

El modelo de recomendación será de tipo no supervisado. La técnica concreta todavía está en fase de estudio y se determinará durante el desarrollo del proyecto.

✨ Funcionalidades
🎥 Recomendación basada en películas

El usuario podrá introducir una o varias películas que le hayan gustado.

El sistema utilizará esa información para encontrar películas con características similares y generar una lista de recomendaciones.

🎯 Recomendación basada en preferencias

El usuario podrá definir sus preferencias cinematográficas para obtener recomendaciones personalizadas.

Entre las características que podrían utilizarse se encuentran:

Géneros, Actores, Directores, Palabras clave, Año de lanzamiento, Valoración, Popularidad, Sinopsis

Otras características disponibles en los datos de TMDB

🔍 Información de las películas

Las películas mostradas podrán incluir información como:

Título, Póster, Sinopsis, Géneros, Fecha de estreno, Valoración, Popularidad, Reparto, Director

La información se obtendrá mediante la API de The Movie Database.

🤖 Sistema de recomendación

El proyecto utilizará un algoritmo de aprendizaje no supervisado para encontrar relaciones y similitudes entre películas.

Actualmente, el modelo concreto todavía no está definido. Durante el desarrollo se estudiarán diferentes alternativas y se seleccionará la que mejor se adapte a las características del proyecto y de los datos disponibles.

Algunas técnicas que podrían estudiarse son:

K-Means, Clustering jerárquico, DBSCAN, Técnicas de reducción de dimensionalidad

⚠️ Nota: estas técnicas son posibilidades a estudiar y no representan todavía la implementación definitiva del proyecto.

🌐 Aplicación web

La aplicación estará desarrollada utilizando principalmente:

Tecnología	Uso
🐍 Python	Lógica de la aplicación y sistema de recomendación
🌐 HTML	Estructura de las páginas web
🎨 CSS	Diseño y estilos de la interfaz
🎬 TMDB API	Obtención de información sobre películas
🤖 Cohere API	Integración futura de funcionalidades basadas en IA (posiblemente)

El framework web de Python se determinará durante el desarrollo del proyecto.

🧠 Posible integración de IA

Como funcionalidad futura, se plantea integrar la API de Cohere para añadir funcionalidades basadas en inteligencia artificial.

Esta integración todavía se encuentra en fase de planificación. Algunas posibilidades que se estudiarán son:

💬 Permitir recomendaciones mediante lenguaje natural.

📝 Analizar las preferencias escritas por el usuario.

🎬 Generar explicaciones sobre por qué se recomienda una película.

🔎 Mejorar la búsqueda de películas a partir de descripciones.

💡 Crear un sistema de interacción más natural con el usuario.

La implementación dependerá de las posibilidades que ofrezca la API y de su integración con el sistema de recomendación principal.

🗄️ Fuente de datos

Los datos utilizados por el proyecto se obtendrán de:

🎬 The Movie Database (TMDB)

TMDB proporciona información sobre películas, series, actores, directores, géneros, imágenes y otros metadatos relacionados con contenido audiovisual.

La aplicación utilizará su API para obtener y consultar esta información.

Este proyecto utiliza datos proporcionados por TMDB y debe cumplir las condiciones de uso y atribución establecidas por su API.

🏗️ Arquitectura prevista

De forma general, el proyecto seguirá una arquitectura similar a:
```text
┌─────────────────────┐
│       Usuario       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│     Interfaz Web    │
│    HTML + CSS       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│    Backend Python   │
└──────────┬──────────┘
           │
      ┌────┴─────┐
      ▼          ▼
┌───────────┐ ┌──────────────┐
│ Sistema de │ │  TMDB API    │
│recomendación│ │              │
└─────┬─────┘ └──────┬───────┘
      │              │
      └──────┬───────┘
             ▼
   ┌───────────────────┐
   │   Recomendaciones │
   │     de películas  │
   └───────────────────┘


En una futura versión, la arquitectura podría incorporar:

                 ┌───────────────┐
                 │   Cohere API  │
                 └───────┬───────┘
                         │
                         ▼
┌─────────┐       ┌──────────────┐
│ Usuario │──────▶│ Backend      │
└─────────┘       │ Python       │
                  └──────┬───────┘
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
       ┌──────────────┐      ┌─────────────┐
       │ Recomendador │      │   TMDB API  │
       └──────────────┘      └─────────────┘

📂 Estructura del proyecto

La estructura definitiva podrá cambiar a medida que avance el desarrollo, pero inicialmente se plantea algo similar a:

movie-recommender/
│
├── app/
│   ├── templates/
│   │   ├── index.html
│   │   ├── recommendations.html
│   │   └── movie.html
│   │
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   └── images/
│   │
│   ├── recommender/
│   │   ├── model.py
│   │   ├── preprocessing.py
│   │   └── similarity.py
│   │
│   ├── tmdb/
│   │   └── api.py
│   │
│   └── routes.py
│
├── data/
│   └── README.md
│
├── tests/
│
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
└── run.py
```
🚀 Instalación
1. Clonar el repositorio
git clone https://github.com/Proyectos-UE/Proyecto-infraestructura.git
cd movie-recommender

(todavia no se ha hecho, para hacer a futuro)

3. Crear un entorno virtual usando miniconda con el comando
conda create -n "nombre del entorno"


3. Instalar las dependencias dentro del entorno
pip install -r requirements.txt

(todavia no se ha hecho, para hacer a futuro)
5. Configurar las variables de entorno

Crear un archivo .env en la raíz del proyecto:

TMDB_API_KEY=tu_api_key
COHERE_API_KEY=tu_api_key


La variable COHERE_API_KEY solamente será necesaria cuando se implemente la integración con Cohere.

Nunca se deben subir las claves de las APIs al repositorio.

▶️ Ejecución

Una vez instaladas las dependencias y configuradas las variables de entorno:

python run.py


Después, abrir la aplicación desde el navegador.

🛣️ Roadmap

El proyecto se encuentra actualmente en desarrollo.

🟢 Fase 1 — Planificación

  - Definir la idea del proyecto

  - Seleccionar TMDB como fuente de datos

  - Definir el uso de aprendizaje no supervisado

  - Analizar los datos disponibles

  - Determinar las variables que utilizará el recomendador

🟡 Fase 2 — Obtención y preparación de datos

  - Conectar con la API de TMDB

  - Obtener información de películas

  - Limpiar los datos

  - Seleccionar las características relevantes

 Transformar los datos para utilizarlos en el modelo

🟡 Fase 3 — Sistema de recomendación

  - Estudiar diferentes algoritmos no supervisados

  - Implementar diferentes alternativas

  - Evaluar los resultados

  - Seleccionar la técnica utilizada

  - Implementar recomendaciones basadas en una película

  - Implementar recomendaciones basadas en varias películas

  - Implementar recomendaciones basadas en preferencias

🟠 Fase 4 — Aplicación web

  - Crear la interfaz principal

  - Implementar búsqueda de películas

  - Permitir seleccionar películas favoritas

  - Mostrar recomendaciones

  - Mostrar información detallada de las películas

 - Mejorar el diseño y la experiencia de usuario

🔵 Fase 5 — Inteligencia artificial

  - Investigar integración con Cohere

  - Diseñar posibles funcionalidades

  - Integrar Cohere API

 - Añadir interacción mediante lenguaje natural

  - Evaluar la utilidad de la IA dentro del sistema

🟣 Fase 6 — Mejoras

 - Optimizar el sistema de recomendación

 - Mejorar el rendimiento

  - Añadir tests

  - Mejorar la interfaz

  - Documentar el proyecto

  - Preparar el despliegue

📊 Posibles criterios de recomendación

Dependiendo de los datos disponibles y del modelo finalmente seleccionado, las recomendaciones podrían tener en cuenta diferentes características:

                    ┌──────────────┐
                    │   Película   │
                    └──────┬───────┘
                           │
       ┌───────────┬───────┼───────────┬───────────┐
       ▼           ▼       ▼           ▼           ▼
    Géneros    Actores  Director   Keywords     Sinopsis
       │           │       │           │           │
       └───────────┴───────┴───────────┴───────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Sistema de      │
                  │ recomendación   │
                  └────────┬────────┘
                           │
                           ▼
                 🎬 Películas similares


La importancia de cada característica dependerá de los resultados obtenidos durante la fase de experimentación.

🧪 Evaluación

Uno de los objetivos del proyecto será analizar la calidad de las recomendaciones obtenidas.

Para ello se estudiarán diferentes métricas y métodos de evaluación adecuados al tipo de sistema implementado.

También se podrán realizar pruebas utilizando diferentes combinaciones de características para analizar cómo afectan a las recomendaciones.

🔐 Seguridad

Las claves de las APIs se almacenarán mediante variables de entorno y no se incluirán directamente en el código fuente.

El archivo .env deberá estar incluido en .gitignore:

.env
.venv/
__pycache__/
*.pyc

🤝 Contribución

Para contribuir:

1. Haz un clon del repositorio.
   git clone [https://github.com/Proyectos-UE/Proyecto-infraestructura.git](https://github.com/Proyectos-UE/Proyecto-infraestructura.git)

2. Crea una nueva rama y cambiáte a esta de manera automática:
   git switch -c rama_ejemplo
   Cada vez que te quieras cambiar a una rama usar comando:
   git switch nombre_rama
   Para comprobar la rama, sale abajo a la izquiera o usar comando:
   git branch
   
3. Comprueba que estas conectado correctamente:
   git remote -v
4. Comprueba que tienes el proyecto actualizado usando fetch:
   - Si estas en la rama_ejemplo:
     git switch main
     git pull origin main
     git switch rama_ejemplo
     git merge main
   - Si ya estas en la rama main (que no deberías):
     git pull origin main


5. Realiza tus cambios.
6. Añadir tus cambias usando:
   git add nombre_del_archivo
   o:
   git add . (para cambiar todos los archivos)

7. Haz commit de los cambios:
   git commit -m "feat: añadir nueva funcionalidad"


8. Sube la rama:
   git push -u origin rama_ejemplo


9. Abre un Pull Request y resolver posibles conflictos.


📚 Tecnologías

🐍 Python

🌐 HTML

🎨 CSS

🤖 Machine Learning — Aprendizaje no supervisado

🎬 The Movie Database (TMDB) API

🤖 Cohere API — planificado

🧪 Testing — por definir

👥 Equipo

Proyecto desarrollado por:

- Andrea Belaunzaran

- Ashley Harris

- Anastasia Lagüera 

- Iñigo Erce 

🎬 Estado del proyecto:

🚧 En desarrollo

El sistema de recomendación, la arquitectura definitiva y la integración con inteligencia artificial se encuentran todavía en fase de investigación y desarrollo.

<p align="center"> 🎬 <strong>Movie Recommendation System</strong> <br> <sub>Encuentra tu próxima película favorita.</sub> </p>


# API REST de Películas (FastAPI + Uvicorn) - Entregable 1

## Instrucciones de Ejecución Local

1. Instalar las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

2. Configurar las variables de entorno:
   Copiar `.env.example` a `.env` y definir la clave secreta:
   ```bash
   SECRET_API_KEY=mi_token_secreto_123
   ```

3. Ejecutar el servidor Uvicorn:
   ```bash
   python app/app.py
   ```
   O alternativamente desde el módulo app:
   ```bash
   uvicorn app.app:app --reload
   ```

4. Acceder a la documentación OpenAPI interactiva (Swagger UI) en:
   `http://127.0.0.1:8000/docs`

---

## Ejemplos de Peticiones y Casos de Prueba

### 1. Petición Correcta (Sin Autenticación)
* **GET** `/api/movies?page=1`
* **cURL:**
  ```bash
  curl -X GET "[http://127.0.0.1:8000/api/movies?page=1](http://127.0.0.1:8000/api/movies?page=1)"
  ```
* **Respuesta Esperada (200 OK):**
  ```json
  {
    "page": 1,
    "results": [
      {"id": 1, "title": "Inception", "year": 2010},
      {"id": 2, "title": "Interstellar", "year": 2014}
    ]
  }
  ```

---

### 2. Petición con Parámetro Inválido (Validación Pydantic)
* **GET** `/api/movies?page=0` (El parámetro debe ser >= 1)
* **cURL:**
  ```bash
  curl -X GET "[http://127.0.0.1:8000/api/movies?page=0](http://127.0.0.1:8000/api/movies?page=0)"
  ```
* **Respuesta Esperada (422 Unprocessable Entity):**
  ```json
  {
    "detail": [
      {
        "type": "greater_than_equal",
        "loc": ["query", "page"],
        "msg": "Input should be greater than or equal to 1"
      }
    ]
  }
  ```

---

### 3. Petición Protegida Correcta (Con Autenticación)
* **POST** `/api/favorites`
* **cURL:**
  ```bash
  curl -X POST "[http://127.0.0.1:8000/api/favorites](http://127.0.0.1:8000/api/favorites)" \
       -H "Content-Type: application/json" \
       -H "Authorization: Bearer mi_token_secreto_123" \
       -d '{"movie_id": 1}'
  ```
* **Respuesta Esperada (201 Created):**
  ```json
  {
    "message": "Película añadida a favoritos con éxito",
    "movie_id": 1
  }
  ```

---

### 4. Petición Sin Autenticación (401 Unauthorized)
* **POST** `/api/favorites`
* **cURL:**
  ```bash
  curl -X POST "[http://127.0.0.1:8000/api/favorites](http://127.0.0.1:8000/api/favorites)" \
       -H "Content-Type: application/json" \
       -d '{"movie_id": 1}'
  ```
* **Respuesta Esperada (401 Unauthorized):**
  ```json
  {
    "detail": "Not authenticated"
  }
  ```

---

### 5. Petición con Token Incorrecto (403 Forbidden)
* **POST** `/api/favorites`
* **cURL:**
  ```bash
  curl -X POST "[http://127.0.0.1:8000/api/favorites](http://127.0.0.1:8000/api/favorites)" \
       -H "Content-Type: application/json" \
       -H "Authorization: Bearer token_falso" \
       -d '{"movie_id": 1}'
  ```
* **Respuesta Esperada (403 Forbidden):**
  ```json
  {
    "detail": "Acceso no autorizado: Token inválido"
  }
  ```