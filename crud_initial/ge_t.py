from fastapi import FastAPI

from fastapi import Query

app = FastAPI(title='mi_primer_crud')

@app.get('/users/{user}/{mensaje}')
def saludar(user: str, mensaje: str):
 
    return {"mensaje": f"Hola {user}, {mensaje}"}

@app.get('/validar/')
def validar(
    nombre: str = Query(None, min_length=3, max_length=50, title="Nombre del usuario", description="El nombre debe tener entre 3 y 50 caracteres", example="Juan"),

):
    return {"mensaje": f"Hola {nombre}, tu nombre es válido"}


users = ['fran','kevin','ana','luis']

@app.get('/users/{id_usuario}')
def obtener_usuario(
    id_usuario: int, 
    moneda: str = Query(None, min_length=3, max_length=3, title="Moneda", description="solo BOB o USD"),
):
    return {"id_usuario": f"{users[id_usuario]}", "moneda": f"{moneda}"}