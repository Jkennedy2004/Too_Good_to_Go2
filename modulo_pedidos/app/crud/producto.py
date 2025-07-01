from sqlalchemy.orm import Session
from app.models.producto import Producto
from app.schemas.producto import ProductoCreate, ProductoUpdate

def crear_producto(db: Session, producto: ProductoCreate):
    nuevo_producto = Producto(**producto.dict())
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto

def obtener_productos(db: Session):
    return db.query(Producto).all()

def obtener_producto_por_id(db: Session, producto_id: int):
    return db.query(Producto).filter(Producto.id == producto_id).first()

def actualizar_producto(db: Session, producto_id: int, producto_data: ProductoUpdate):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if producto:
        for field, value in producto_data.dict(exclude_unset=True).items():
            setattr(producto, field, value)
        db.commit()
        db.refresh(producto)
    return producto

def eliminar_producto(db: Session, producto_id: int):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if producto:
        db.delete(producto)
        db.commit()
    return producto