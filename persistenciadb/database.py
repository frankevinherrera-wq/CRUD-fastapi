from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


url = "sqlite:///./sql_app.db"
engine = create_engine(
    url, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

