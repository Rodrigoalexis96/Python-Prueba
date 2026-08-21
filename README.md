Python-Prueba

API de prueba creada con Python, FastAPI y Uvicorn, preparada para ejecutarse localmente o dentro de un contenedor Docker.

Tecnologías utilizadas
Python 3.14
FastAPI
Uvicorn
Docker
Git y GitHub
Endpoints

La API incluye actualmente las siguientes rutas:

Inicio
GET /

Respuesta:

{
  "mensaje": "Mi primera API funciona correctamente"
}
Estado
GET /estado

Respuesta:

{
  "estado": "activo",
  "servicio": "API Python",
  "version": "1.0"
}
Documentación Swagger
http://localhost:8000/docs
Ejecutar localmente

Crear el entorno virtual:

python -m venv .venv

Activar el entorno virtual en PowerShell:

.\.venv\Scripts\Activate.ps1

Instalar las dependencias:

pip install -r requirements.txt

Ejecutar la API:

python -m uvicorn app:app --reload

Abrir en el navegador:

http://127.0.0.1:8000

Documentación:

http://127.0.0.1:8000/docs
Ejecutar con Docker

Construir la imagen:

docker build -t python-api-prueba .

Crear y ejecutar el contenedor:

docker run -d -p 8000:8000 --name python-api-prueba-container python-api-prueba

Abrir la API:

http://localhost:8000

Abrir Swagger:

http://localhost:8000/docs

Ver el estado del contenedor:

docker ps

Ver los logs:

docker logs python-api-prueba-container

Detener el contenedor:

docker stop python-api-prueba-container

Volver a iniciarlo:

docker start python-api-prueba-container
Estructura del proyecto
Python-Prueba/
├── .dockerignore
├── .gitignore
├── Dockerfile
├── app.py
├── README.md
└── requirements.txt
Objetivo

Este proyecto fue creado como práctica para comprender el flujo básico de desarrollo de una API:

Python
   ↓
FastAPI
   ↓
Uvicorn
   ↓
Docker
   ↓
Git
   ↓
GitHub