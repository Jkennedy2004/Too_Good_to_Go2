from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Producto(Base):
    _tablename_ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String)
    precio = Column(Float, nullable=False)
    restaurante_id = Column(Integer, ForeignKey("restaurantes.id"), nullable=False)

    restaurante = relationship("Restaurante", backref="productos")