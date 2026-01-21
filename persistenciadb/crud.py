from sqlalchemy.orm import Session
from . import models, schemas

# Función para buscar un usuario por ID
def get_user(db: Session, user_id: int):
    # SELECT * FROM usuarios WHERE id = user_id LIMIT 1
    return db.query(models.UserDB).filter(models.UserDB.id == user_id).first()

# Función para obtener todos los usuarios
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.UserDB).offset(skip).limit(limit).all()

# Función para crear un usuario
def create_user(db: Session, user: schemas.UserCreate):
    # Creamos la instancia del modelo de SQLAlchemy
    db_user = models.UserDB(nombre=user.nombre, edad=user.edad)
    
    db.add(db_user)      # Lo preparamos para la base de datos
    db.commit()          # Guardamos los cambios permanentemente
    db.refresh(db_user)  # Refrescamos para obtener el ID generado por SQL
    
    return db_user