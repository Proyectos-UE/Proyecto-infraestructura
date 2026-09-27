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

Géneros

Actores

Directores

Palabras clave

Año de lanzamiento

Valoración

Popularidad

Sinopsis

Otras características disponibles en los datos de TMDB

🔍 Información de las películas

Las películas mostradas podrán incluir información como:

Título

Póster

Sinopsis

Géneros

Fecha de estreno

Valoración

Popularidad

Reparto

Director

La información se obtendrá mediante la API de The Movie Database.

🤖 Sistema de recomendación

El proyecto utilizará un algoritmo de aprendizaje no supervisado para encontrar relaciones y similitudes entre películas.

Actualmente, el modelo concreto todavía no está definido. Durante el desarrollo se estudiarán diferentes alternativas y se seleccionará la que mejor se adapte a las características del proyecto y de los datos disponibles.

Algunas técnicas que podrían estudiarse son:

K-Means

Clustering jerárquico

DBSCAN

Similitud del coseno

Técnicas de reducción de dimensionalidad

Sistemas de recomendación basados en contenido

⚠️ Nota: estas técnicas son posibilidades a estudiar y no representan todavía la implementación definitiva del proyecto.

🌐 Aplicación web

La aplicación estará desarrollada utilizando principalmente:

Tecnología	Uso
🐍 Python	Lógica de la aplicación y sistema de recomendación
🌐 HTML	Estructura de las páginas web
🎨 CSS	Diseño y estilos de la interfaz
🎬 TMDB API	Obtención de información sobre películas
🤖 Cohere API	Integración futura de funcionalidades basadas en IA

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

🚀 Instalación
1. Clonar el repositorio
git clone https://github.com/USERNAME/movie-recommender.git
cd movie-recommender

2. Crear un entorno virtual
python -m venv venv


Activar el entorno virtual:

Windows

venv\Scripts\activate


Linux / macOS

source venv/bin/activate

3. Instalar las dependencias
pip install -r requirements.txt

4. Configurar las variables de entorno

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

 Definir la idea del proyecto

 Seleccionar TMDB como fuente de datos

 Definir el uso de aprendizaje no supervisado

 Analizar los datos disponibles

 Determinar las variables que utilizará el recomendador

🟡 Fase 2 — Obtención y preparación de datos

 Conectar con la API de TMDB

 Obtener información de películas

 Limpiar los datos

 Seleccionar las características relevantes

 Transformar los datos para utilizarlos en el modelo

🟡 Fase 3 — Sistema de recomendación

 Estudiar diferentes algoritmos no supervisados

 Implementar diferentes alternativas

 Evaluar los resultados

 Seleccionar la técnica utilizada

 Implementar recomendaciones basadas en una película

 Implementar recomendaciones basadas en varias películas

 Implementar recomendaciones basadas en preferencias

🟠 Fase 4 — Aplicación web

 Crear la interfaz principal

 Implementar búsqueda de películas

 Permitir seleccionar películas favoritas

 Mostrar recomendaciones

 Mostrar información detallada de las películas

 Mejorar el diseño y la experiencia de usuario

🔵 Fase 5 — Inteligencia artificial

 Investigar integración con Cohere

 Diseñar posibles funcionalidades

 Integrar Cohere API

 Añadir interacción mediante lenguaje natural

 Evaluar la utilidad de la IA dentro del sistema

🟣 Fase 6 — Mejoras

 Optimizar el sistema de recomendación

 Mejorar el rendimiento

 Añadir tests

 Mejorar la interfaz

 Documentar el proyecto

 Preparar el despliegue

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
venv/
__pycache__/
*.pyc

🤝 Contribución

Las contribuciones son bienvenidas.

Para contribuir:

Haz un fork del repositorio.

Crea una nueva rama:

git checkout -b feature/nueva-funcionalidad


Realiza tus cambios.

Haz commit de los cambios:

git commit -m "feat: añadir nueva funcionalidad"


Sube la rama:

git push origin feature/nueva-funcionalidad


Abre un Pull Request.

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

Andrea Belaunzaran

Ashley Harris

Anastasia Lagüera 

Iñigo Erce 

📄 Licencia

Este proyecto se desarrolla con fines educativos.

La licencia definitiva del proyecto se determinará durante el desarrollo.

🎬 Estado del proyecto

🚧 En desarrollo

El sistema de recomendación, la arquitectura definitiva y la integración con inteligencia artificial se encuentran todavía en fase de investigación y desarrollo.

<p align="center"> 🎬 <strong>Movie Recommendation System</strong> <br> <sub>Encuentra tu próxima película favorita.</sub> </p>