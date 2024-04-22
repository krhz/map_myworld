# Map My World API

API para explorar y revisar diferentes ubicaciones y categorías del mundo.

## Descripción

Este proyecto implementa una API utilizando FastAPI para permitir a los usuarios explorar y revisar ubicaciones y categorías específicas del mundo, como restaurantes, parques y museos. La API proporciona endpoints para gestionar ubicaciones, categorías, revisiones y funcionalidades de exploración de combinaciones no revisadas.

## Tecnologías Utilizadas

- FastAPI
- Python 3.x
- Uvicorn

## Estructura del Proyecto

my_fastapi_project/
├── app/
│ ├── init.py
│ ├── api/
│ │ ├── init.py
│ │ ├── locations.py
│ │ ├── categories.py
│ │ ├── reviews.py
│ │ └── explore.py
│ └── main.py
├── venv/ (entorno virtual)
├── requirements.txt
└── README.md

## Requisitos

- Python 3.x
- pip (administrador de paquetes de Python)

## Accede al directorio del proyecto

`cd map-my-world-api`

## Crea y activa un entorno virtual (opcional pero recomendado)

`python3 -m venv venv\nsource venv/bin/activate   # En Linux/macOS\nvenv\Scripts\activate      # En Windows`

## Instala las dependencias

`pip install -r requirements.txt`

## Uso

`uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload`

## Accede a la documentación interactiva (Swagger UI) en tu navegador

`Accede a la documentación interactiva (Swagger UI) en tu navegador:`

## Endpoints Principales

- /api/locations/: Gestión de ubicaciones.
- /api/categories/: Gestión de categorías.
- /api/reviews/: Gestión de revisiones de ubicaciones por categoría.
- /api/explore/: Funcionalidad de exploración de combinaciones no revisadas.
