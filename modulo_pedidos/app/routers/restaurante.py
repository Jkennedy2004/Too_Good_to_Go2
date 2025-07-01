from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.restaurante import RestauranteCreate, RestauranteOut, RestauranteUpdate
from app.crud import crud_restaurante
from app.database import SessionLocal

router = APIRouter(prefix="/restaurantes", tags=["restaurantes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=RestauranteOut, status_code=status.HTTP_201_CREATED)
def crear_restaurante(restaurante: RestauranteCreate, db: Session = Depends(get_db)):
    return crud_restaurante.crear_restaurante(db, restaurante)

@router.get("/", response_model=List[RestauranteOut])
def listar_restaurantes(db: Session = Depends(get_db)):
    return crud_restaurante.obtener_restaurantes(db)

@router.get("/{restaurante_id}", response_model=RestauranteOut)
def obtener_restaurante(restaurante_id: int, db: Session = Depends(get_db)):
    restaurante = crud_restaurante.obtener_restaurante_por_id(db, restaurante_id)
    if not restaurante:
        raise HTTPException(status_code=404, detail="Restaurante no encontrado")
    return restaurante

@router.put("/{restaurante_id}", response_model=RestauranteOut)
def actualizar_restaurante(restaurante_id: int, restaurante_data: RestauranteUpdate, db: Session = Depends(get_db)):
    restaurante = crud_restaurante.actualizar_restaurante(db, restaurante_id, restaurante_data)
    if not restaurante:
        raise HTTPException(status_code=404, detail="Restaurante no encontrado")
    return restaurante

@router.delete("/{restaurante_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_restaurante(restaurante_id: int, db: Session = Depends(get_db)):
    restaurante = crud_restaurante.eliminar_restaurante(db, restaurante_id)
    if not restaurante:
        raise HTTPException(status_code=404, detail="Restaurante no encontrado")