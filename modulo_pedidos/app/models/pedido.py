from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Pedido(Base):
    _tablename_ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    fecha_pedido = Column(DateTime, default=datetime.utcnow)

    usuario = relationship("Usuario", backref="pedidos")
    detalles = relationship("DetallePedido", back_populates="pedido")
    detalles = relationship("DetallePedido", back_populates="pedido", cascade="all, delete")