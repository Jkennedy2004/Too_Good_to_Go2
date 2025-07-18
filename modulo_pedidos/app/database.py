from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Reemplaza con tus propias credenciales
SQLALCHEMY_DATABASE_URL = "postgresql://usuario:contraseña@localhost:5432/nombre_basedatos"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()