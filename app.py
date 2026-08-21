from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "Mi primera API funciona correctamente"}

@app.get("/estado")
def estado():
    return {
        "estado": "activo",
        "servicio": "API Python",
        "version": "1.0"
    }