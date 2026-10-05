# 🎬 Sistema de Recomendación de Películas

Sistema web de recomendación de películas que genera sugerencias personalizadas a partir de las preferencias e interacciones de los usuarios.

El proyecto utiliza **FastAPI** como backend, **HTML y CSS** para la interfaz web y **The Movie Database (TMDB) API** para obtener información actualizada sobre películas.

Las preferencias e interacciones de los usuarios registrados se almacenarán en una base de datos y serán utilizadas por el sistema de recomendación para generar sugerencias personalizadas.

## 📌 Descripción

El objetivo del proyecto es desarrollar una plataforma capaz de recomendar películas adaptándose a los gustos de cada usuario.

La aplicación permitirá buscar películas y consultar su información utilizando los datos proporcionados por TMDB.

Los usuarios registrados también podrán indicar sus preferencias mediante sus interacciones con las películas, principalmente:

- ⭐ Añadir películas a una lista de películas que les han gustado.
- 🔖 Añadir películas a una lista de películas que quieren ver en el futuro.

Estas interacciones se almacenarán en la base de datos asociadas al usuario y podrán utilizarse como variables para generar recomendaciones personalizadas.

La lista de películas que han gustado al usuario representa una señal directa de preferencia, mientras que la lista de películas pendientes de ver representa una señal de interés.

## ✨ Funcionalidades

### 🔎 Búsqueda de películas

Los usuarios podrán buscar películas por título.

La aplicación realizará la consulta a través de la API de TMDB y mostrará los resultados en la interfaz web.

La búsqueda será una funcionalidad pública y no requerirá que el usuario haya iniciado sesión.

### 🎬 Información de las películas

Los usuarios podrán consultar información obtenida mediante TMDB, como:

- Título
- Póster
- Sinopsis
- Géneros
- Fecha de estreno
- Valoración
- Popularidad
- Reparto
- Director

### ⭐ Películas que me gustan

Los usuarios autenticados podrán añadir películas a una lista personal de películas que les han gustado.

Esta información se almacenará en la base de datos y podrá utilizarse como una señal de preferencia para el sistema de recomendación.

### 🔖 Lista de películas para ver

Los usuarios autenticados podrán guardar películas que quieran ver en el futuro.

Esta información también se almacenará en la base de datos. Se considerará una señal de interés diferente de una película marcada explícitamente como favorita o que le haya gustado al usuario.

### 🤖 Sistema de recomendación

El sistema utilizará las preferencias e interacciones almacenadas para generar recomendaciones personalizadas.

Entre las variables que podrán utilizarse se encuentran:

- Películas que le han gustado al usuario.
- Películas guardadas para ver posteriormente.
- Géneros.
- Actores.
- Directores.
- Palabras clave.
- Valoración.
- Popularidad.
- Otras características obtenidas mediante TMDB.

El sistema de recomendación utilizará técnicas de aprendizaje no supervisado. Durante el desarrollo se estudiarán y compararán diferentes alternativas para seleccionar la técnica más adecuada.

Entre las técnicas consideradas se encuentran:

- K-Means.
- Clustering jerárquico.
- DBSCAN.
- Técnicas de reducción de dimensionalidad.

## 🌐 API y aplicación web

El backend de la aplicación está desarrollado utilizando **FastAPI**.

FastAPI gestiona los endpoints de la aplicación y genera automáticamente documentación OpenAPI.

La documentación interactiva puede consultarse durante la ejecución local en:

`/docs`

La aplicación diferencia entre recursos públicos y recursos que requieren autenticación.

### Recursos públicos

Los usuarios podrán acceder sin autenticación a funcionalidades como:

- Página principal.
- Búsqueda de películas.
- Consulta de información cinematográfica.

La información sobre las películas se obtiene mediante la API externa de TMDB.

### Recursos protegidos

Las operaciones asociadas a información personal del usuario requerirán autenticación.

Entre ellas:

- Añadir o eliminar películas de la lista de películas que le gustan.
- Añadir o eliminar películas de la lista de películas para ver.
- Consultar las preferencias almacenadas del usuario.
- Obtener recomendaciones personalizadas cuando estas dependan de información asociada al usuario.

La aplicación también dispone de recursos administrativos protegidos mediante credenciales específicas.

## 🏗️ Arquitectura

La arquitectura general del proyecto será:

```text
                    ┌─────────────────┐
                    │     Usuario     │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   HTML + CSS    │
                    │  Interfaz web   │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │     FastAPI     │
                    │     Backend     │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
        ┌──────────┐   ┌──────────┐   ┌──────────────┐
        │ TMDB API │   │ Base de  │   │ Recomendador │
        │          │   │  datos   │   │              │
        └──────────┘   └──────────┘   └──────────────┘
                             │              ▲
                             │              │
                             └──────────────┘
                         Preferencias e
                          interacciones
```

TMDB proporciona la información cinematográfica.

La API propia de la aplicación gestiona las funcionalidades internas, incluyendo las interacciones de los usuarios y el acceso a los datos almacenados.

La base de datos almacena las preferencias e interacciones de los usuarios.

El sistema de recomendación utiliza esta información para generar predicciones y recomendaciones personalizadas.

## 🔐 Seguridad

Las credenciales y claves utilizadas por la aplicación se almacenan mediante variables de entorno y no se incluyen directamente en el código fuente.

El archivo `.env` contiene las credenciales necesarias para ejecutar la aplicación, por ejemplo:

```text
TMDB_API_KEY=...
TMDB_API_TOKEN=...
ADMIN_API_KEY=...
```

El archivo `.env` está incluido en `.gitignore` y no debe subirse al repositorio.

La aplicación diferencia entre endpoints públicos y protegidos.

Los endpoints públicos permiten realizar operaciones que no acceden a información privada, como buscar películas.

Los recursos administrativos están protegidos mediante una API Key enviada mediante la cabecera `X-API-Key`. Si las credenciales no se proporcionan o son incorrectas, la API devuelve un código HTTP `401 Unauthorized`.

Las operaciones asociadas a información personal del usuario, como sus películas favoritas o su lista de películas pendientes, requerirán autenticación del usuario cuando dichas funcionalidades sean implementadas.

## ⚠️ Gestión de errores

Las llamadas realizadas a servicios externos incluyen tratamiento controlado de errores.

La aplicación contempla situaciones como:

- Timeout en una petición externa.
- Errores HTTP devueltos por TMDB.
- Problemas de conexión.
- Respuestas JSON no válidas.
- Falta de credenciales para acceder a recursos protegidos.

Cuando TMDB no está disponible, la aplicación devuelve un error controlado `503 Service Unavailable` en lugar de producir un error interno no gestionado.

Los intentos de acceso a recursos protegidos sin las credenciales necesarias devuelven `401 Unauthorized`.

## 📝 Validación

FastAPI realiza la validación de los parámetros recibidos por los endpoints.

Los parámetros obligatorios que no se proporcionan correctamente generan respuestas HTTP de tipo `4xx`, evitando procesar peticiones con datos inválidos.

Se podrán añadir restricciones adicionales dependiendo de los datos requeridos por cada endpoint.

## 📖 Documentación OpenAPI

FastAPI genera automáticamente la especificación OpenAPI de la aplicación.

Durante la ejecución local, la documentación interactiva puede consultarse mediante:

`http://127.0.0.1:8000/docs`

Desde esta interfaz es posible consultar los endpoints disponibles, sus parámetros y códigos de respuesta, así como probar las operaciones de la API.

Los endpoints protegidos permiten comprobar desde esta documentación el comportamiento de la aplicación con y sin credenciales.

## 🗄️ Diseño de la base de datos

La aplicación utilizará una base de datos para almacenar la información de los usuarios y sus interacciones con las películas.

El objetivo es que estas interacciones puedan utilizarse posteriormente como información de entrada para el sistema de recomendación.

### 📊 Estructura general

La base de datos estará formada inicialmente por cuatro tablas principales:

- `usuarios`: almacena la información de cada usuario registrado.
- `peliculas`: almacena las películas utilizadas por la aplicación.
- `favoritos`: relaciona cada usuario con las películas que ha marcado como favoritas.
- `watchlist`: relaciona cada usuario con las películas que quiere ver en el futuro.

La relación entre las tablas sería:

```text
                         ┌──────────────────────┐
                         │       USUARIOS       │
                         ├──────────────────────┤
                         │ 🔑 id_usuario (PK)   │
                         │    nombre            │
                         │    email             │
                         │    password_hash     │
                         └──────────┬───────────┘
                                    │
                         1          │          1
                      ┌─────────────┴─────────────┐
                      │                           │
                      │ N                         │ N
             ┌────────▼─────────┐       ┌────────▼─────────┐
             │    FAVORITOS     │       │    WATCHLIST     │
             ├──────────────────┤       ├──────────────────┤
             │ 🔗 id_usuario FK │       │ 🔗 id_usuario FK │
             │ 🔗 id_pelicula FK│       │ 🔗 id_pelicula FK│
             │    fecha         │       │    fecha         │
             └────────┬─────────┘       └────────┬─────────┘
                      │ N                         │ N
                      │                           │
                      └─────────────┬─────────────┘
                                    │
                                    │ 1
                         ┌──────────▼───────────┐
                         │      PELICULAS       │
                         ├──────────────────────┤
                         │ 🔑 id_pelicula (PK)  │
                         │    titulo            │
                         │    genero            │
                         │    director          │
                         │    popularidad       │
                         │    valoracion        │
                         │    ...               │
                         └──────────────────────┘
```

`PK` representa una **Primary Key (clave primaria)** y `FK` una **Foreign Key (clave foránea)**.

---

### 👤 Tabla `usuarios`

Esta tabla identifica a cada usuario registrado en la aplicación.

| Campo | Descripción |
|---|---|
| `id_usuario` | Identificador único del usuario |
| `nombre` | Nombre del usuario |
| `email` | Email utilizado para iniciar sesión |
| `password_hash` | Hash de la contraseña |

La contraseña no se almacenará directamente. Se almacenará únicamente su hash como medida de seguridad.

---

### 🎬 Tabla `peliculas`

Contendrá la información necesaria de las películas utilizadas por la aplicación.

| Campo | Descripción |
|---|---|
| `id_pelicula` | Identificador único de la película |
| `titulo` | Título |
| `genero` | Género o géneros |
| `director` | Director |
| `popularidad` | Popularidad |
| `valoracion` | Valoración |
| `...` | Otras variables necesarias para el recomendador |

La información cinematográfica se obtendrá principalmente mediante la API de TMDB.

El identificador proporcionado por TMDB puede utilizarse para identificar las películas y relacionarlas con las interacciones almacenadas en nuestra base de datos.

---

### ❤️ Tabla `favoritos`

Esta tabla permite registrar qué películas le han gustado a cada usuario.

| id_usuario | id_pelicula | fecha |
|---:|---:|---|
| 1 | 101 | 2026-10-05 |
| 1 | 103 | 2026-10-05 |
| 2 | 101 | 2026-10-06 |

Por ejemplo:

```text
Usuario 1 ─────❤️─────> Película 101
          └────❤️─────> Película 103

Usuario 2 ─────❤️─────> Película 101
```

Esto representa una relación **muchos a muchos (N:M)**:

- Un usuario puede tener muchas películas favoritas.
- Una película puede ser favorita de muchos usuarios.

La tabla `favoritos` actúa como tabla intermedia entre `usuarios` y `peliculas`.

---

### 🔖 Tabla `watchlist`

Funcionará de manera similar a `favoritos`, pero almacenará las películas que el usuario está interesado en ver en el futuro.

| id_usuario | id_pelicula | fecha |
|---:|---:|---|
| 1 | 105 | 2026-10-05 |
| 1 | 108 | 2026-10-06 |
| 2 | 103 | 2026-10-06 |

La `watchlist` representa **interés**, mientras que `favoritos` representa una señal más directa de que una película le gusta al usuario.

Por este motivo, ambas variables podrán tener un tratamiento diferente dentro del sistema de recomendación.

---

## 🔄 Flujo de los datos

Cuando un usuario interactúa con una película, nuestra API será responsable de almacenar esa interacción en la base de datos.

Por ejemplo:

```text
┌──────────────┐
│   USUARIO    │
└──────┬───────┘
       │
       │ Pulsa ❤️ en una película
       ▼
┌──────────────────┐
│     FastAPI      │
│   Nuestra API    │
└────────┬─────────┘
         │
         │ Identifica al usuario
         │ y la película
         ▼
┌──────────────────┐
│     FAVORITOS    │
├──────────────────┤
│ id_usuario = 1   │
│ id_pelicula = 101│
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  BASE DE DATOS   │
└──────────────────┘
```

De esta forma, las interacciones quedan asociadas al usuario que las ha realizado.

---

## 🤖 Uso de la base de datos para el recomendador

La información almacenada podrá utilizarse posteriormente para construir las variables necesarias para el modelo de recomendación.

```text
              BASE DE DATOS
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
     ❤️ Favoritos        🔖 Watchlist
          │                   │
          └─────────┬─────────┘
                    ▼
            Datos del usuario
                    │
                    ▼
             Preprocesamiento
                    │
                    ▼
          Modelo de recomendación
                    │
                    ▼
        🎬 Películas recomendadas
```

Por ejemplo, a partir de los favoritos de un usuario se podrán analizar características como:

```text
Usuario 1
   │
   ├──❤️ Interstellar
   ├──❤️ Inception
   └──❤️ The Martian
            │
            ▼
    Características comunes
            │
     ┌──────┼────────┐
     ▼      ▼        ▼
   Género Director Keywords ...
            │
            ▼
      RECOMENDADOR
            │
            ▼
   Nuevas películas similares
```

Esto permitirá que el modelo utilice el comportamiento real de cada usuario para generar recomendaciones más personalizadas.

## 🔐 Acceso a los datos

Los usuarios no accederán directamente a la base de datos.

El flujo será:

```text
Usuario
   │
   │ Autenticación
   ▼
FastAPI
   │
   │ Conexión autorizada
   ▼
Base de datos
```

FastAPI será responsable de comprobar la identidad del usuario y determinar qué operaciones puede realizar.

Por ejemplo, un usuario autenticado podrá consultar y modificar sus propios favoritos, pero no los favoritos de otro usuario.

La aplicación utilizará sus propias credenciales para conectarse a la base de datos. Estas credenciales se almacenarán mediante variables de entorno y no directamente en el código fuente.
