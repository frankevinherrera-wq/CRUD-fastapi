from pydantic import BaseModel
from typing import Optional

# Esquema base (lo que tienen en común)
class UserBase(BaseModel):
    nombre: str
    edad: int

# Esquema para CREAR (Lo que el cliente envía)
# No pedimos ID porque SQL lo genera solo
class UserCreate(UserBase):
    pass

# Esquema para DEVOLVER datos (Lo que la API responde)
# Aquí sí incluimos el ID
class User(UserBase):
    id: int

    class Config:
        from_attributes = True # Esto permite que Pydantic lea modelos de SQLAlchemy