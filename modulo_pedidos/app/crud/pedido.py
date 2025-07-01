from sqlalchemy.orm import Session
from app.models.pedido import Pedido
from app.schemas.pedido import PedidoCreate, PedidoUpdate

def crear_pedido(db: Session, pedido: PedidoCreate):
    nuevo_pedido = Pedido(**pedido.dict())
    db.add(nuevo_pedido)
    db.commit()
    db.refresh(nuevo_pedido)
    return nuevo_pedido

def obtener_pedidos(db: Session):
    return db.query(Pedido).all()

def obtener_pedido_por_id(db: Session, pedido_id: int):
    return db.query(Pedido).filter(Pedido.id == pedido_id).first()

def actualizar_pedido(db: Session, pedido_id: int, pedido_data: PedidoUpdate):
    pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()
    if pedido:
        for field, value in pedido_data.dict(exclude_unset=True).items():
            setattr(pedido, field, value)
        db.commit()
        db.refresh(pedido)
    return pedido

def eliminar_pedido(db: Session, pedido_id: int):
    pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()
    if pedido:
        db.delete(pedido)
        db.commit()
    return pedido