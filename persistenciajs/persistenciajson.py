from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os


app = FastAPI(title='persistencia_json')

class User (BaseModel):
    name : str
    age : int


db = './persistencia/users.json'



def load_data():
    if not os.path.exists(db):
        return {}
    with open(db, 'r') as f:
        data = json.load(f)
        return {int(i): j for i, j in data.items()}
    
def save_data(users):
    with open(db, 'w') as f:
        json.dump(users, f, indent = 4)

@app.get('/users/{id}')
def persons (id: int):
    actual = load_data()
    if id in actual:
        return {"mensaje": f"Usuario con ID {id} es {actual[id]}"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")


@app.post('/users/crear')
def crear_usuario (usuario: User):
    current = load_data()
    current[len(current)+1] = usuario.dict()
    save_data(current)
    
    return {
        "mensaje": "Usuario creado con éxito",
        "lista_actualizada": f"{current}"
    }