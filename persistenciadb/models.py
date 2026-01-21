from sqlalchemy import Column, Integer, String
from .database import Base, engine  

class UserDB(Base):
    __tablename__ = "usuarios" 

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    edad = Column(Integer)


print("Creando base de datos...")

Base.metadata.create_all(bind=engine)

print('create')