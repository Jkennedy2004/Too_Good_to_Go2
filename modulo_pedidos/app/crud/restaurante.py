from sqlalchemy.orm import Session
from app.models.restaurante import Restaurante
from app.schemas.restaurante import RestauranteCreate, RestauranteUpdate

def crear_restaurante(db: Session, restaurante: RestauranteCreate):
    nuevo_restaurante = Restaurante(**restaurante.dict())
    db.add(nuevo_restaurante)
    db.commit()
    db.refresh(nuevo_restaurante)
    return nuevo_restaurante

def obtener_restaurantes(db: Session):
    return db.query(Restaurante).all()

def obtener_restaurante_por_id(db: Session, restaurante_id: int):
    return db.query(Restaurante).filter(Restaurante.id == restaurante_id).first()

def actualizar_restaurante(db: Session, restaurante_id: int, restaurante_data: RestauranteUpdate):
    restaurante = db.query(Restaurante).filter(Restaurante.id == restaurante_id).first()
    if restaurante:
        for field, value in restaurante_data.dict(exclude_unset=True).items():
            setattr(restaurante, field, value)
        db.commit()
        db.refresh(restaurante)
    return restaurante

def eliminar_restaurante(db: Session, restaurante_id: int):
    restaurante = db.query(Restaurante).filter(Restaurante.id == restaurante_id).first()
    if restaurante:
        db.delete(restaurante)
        db.commit()
    return restaurante