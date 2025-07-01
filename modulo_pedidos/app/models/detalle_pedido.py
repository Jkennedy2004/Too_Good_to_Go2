from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.database import Base

class DetallePedido(Base):
    _tablename_ = "detalle_pedido"

    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey("pedido.id", ondelete="CASCADE"), nullable=False)
    producto_id = Column(Integer, ForeignKey("producto.id", ondelete="CASCADE"), nullable=False)
    cantidad = Column(Integer, nullable=False)
    subtotal = Column(Float, nullable=False)

    pedido = relationship("Pedido", back_populates="detalles")
    producto = relationship("Producto")