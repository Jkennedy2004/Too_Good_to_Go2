from sqlalchemy import Column, Integer, String
from app.database import Base

class Usuario(Base):
    _tablename_ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    correo = Column(String, unique=True, index=True)
    contrasena = Column(String, nullable=False)