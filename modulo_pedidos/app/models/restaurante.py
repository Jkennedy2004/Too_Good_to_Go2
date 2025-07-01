from sqlalchemy import Column, Integer, String
from app.database import Base

class Restaurante(Base):
    _tablename_ = "restaurantes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    direccion = Column(String, nullable=False)
    telefono = Column(String)