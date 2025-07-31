from pydantic import BaseModel
from typing import Optional

class DetallePedidoBase(BaseModel):
    pedido_id: int
    producto_id: int
    cantidad: int
    subtotal: float

class DetallePedidoCreate(DetallePedidoBase):
    pass

class DetallePedidoUpdate(BaseModel):
    pedido_id: Optional[int] = None
    producto_id: Optional[int] = None
    cantidad: Optional[int] = None
    subtotal: Optional[float] = None

class DetallePedidoOut(DetallePedidoBase):
    id: int

    class Config:
        orm_mode = True