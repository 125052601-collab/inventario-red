from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Inventario de red")


class Dispositivo(BaseModel):
    nombre: str
    tipo: str
    ip: str
    activo: bool = True


inventario = [
    Dispositivo(nombre="R1", tipo="router", ip="10.0.0.1"),
    Dispositivo(nombre="SW1", tipo="switch", ip="10.0.0.2"),
    Dispositivo(nombre="FW1", tipo="firewall", ip="10.0.0.3"),
]


@app.get("/")
async def raiz():
    """Mensaje de bienvenida."""
    return {"mensaje": "API de inventario de red"}


@app.get("/dispositivos")
async def listar():
    """Devuelve todos los equipos."""
    return inventario


@app.get("/dispositivos/{nombre}")
async def obtener(nombre: str):
    """Busca un equipo por su nombre."""
    for equipo in inventario:
        if equipo.nombre.upper() == nombre.upper():
            return equipo
    raise HTTPException(status_code=404,
                        detail=f"No existe el equipo {nombre}")