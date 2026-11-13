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

def buscar(nombre: str) -> Dispositivo | None:
    """Devuelve el equipo con ese nombre, o None si no existe."""
    for equipo in inventario:
        if equipo.nombre.upper() == nombre.upper():
            return equipo
    return None




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
    equipo = buscar(nombre)
    if equipo is None:
        raise HTTPException(status_code=404,
                            detail=f"No existe el equipo {nombre}")
    return equipo