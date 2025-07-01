from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PedidoBase(BaseModel):
    usuario_id: int
    fecha_pedido: Optional[datetime] = None

class PedidoCreate(PedidoBase):
    pass

class PedidoUpdate(BaseModel):
    usuario_id: Optional[int] = None
    fecha_pedido: Optional[datetime] = None

class PedidoOut(PedidoBase):
    id: int

    class Config:
        orm_mode = True