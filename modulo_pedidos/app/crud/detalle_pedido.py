from sqlalchemy.orm import Session
from app.models.detalle_pedido import DetallePedido
from app.schemas.detalle_pedido import DetallePedidoCreate, DetallePedidoUpdate

def crear_detalle_pedido(db: Session, detalle: DetallePedidoCreate):
    nuevo_detalle = DetallePedido(**detalle.dict())
    db.add(nuevo_detalle)
    db.commit()
    db.refresh(nuevo_detalle)
    return nuevo_detalle

def obtener_detalles_pedido(db: Session):
    return db.query(DetallePedido).all()

def obtener_detalles_por_pedido(db: Session, pedido_id: int):
    return db.query(DetallePedido).filter(DetallePedido.pedido_id == pedido_id).all()

def actualizar_detalle_pedido(db: Session, detalle_id: int, detalle_data: DetallePedidoUpdate):
    detalle = db.query(DetallePedido).filter(DetallePedido.id == detalle_id).first()
    if detalle:
        for field, value in detalle_data.dict(exclude_unset=True).items():
            setattr(detalle, field, value)
        db.commit()
        db.refresh(detalle)
    return detalle

def eliminar_detalle_pedido(db: Session, detalle_id: int):
    detalle = db.query(DetallePedido).filter(DetallePedido.id == detalle_id).first()
    if detalle:
        db.delete(detalle)
        db.commit()
    return detalle