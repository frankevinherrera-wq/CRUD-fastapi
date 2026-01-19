from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title='mi_primer_post')

class Persona(BaseModel):
    nombre: str
    edad: int
    ciudad: Optional[str] = None

users = {}

@app.get('/users/{id}')
def persona(id: int):
    if id in users:
        return {"mensaje": f"Usuario con ID {id} es {users[id]}"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")


@app.post("/users/crear")
def crear_usuario(usuario: Persona):
    users[len(users)+1] = usuario.dict()
    return {
        "mensaje": "Usuario creado con éxito",
        "lista_actualizada": users
    }



@app.put("/users/actualizar/")
def actualizar (id: int, usuario: Persona):
    if id in users:
        users[id] = usuario.dict()
       
        return {'mensaje': 'Usuario actualizado con éxito', 'usuario': users[id]}
        
    raise HTTPException(status_code=404, detail="Usuario no encontrado")



@app.delete("/users/eliminar/{id}")
def eliminar_usuario(id: int):
    if id in users:
        nuevo = users.pop(id)
        return {'mensaje': 'Usuario eliminado con éxito', 
                'usuario_eliminado': nuevo, 
                'lista_actualizada': users
                }
    raise HTTPException(status_code=404, detail="Usuario no encontrado")