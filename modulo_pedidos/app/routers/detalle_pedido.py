from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.detalle_pedido import DetallePedidoCreate, DetallePedidoOut, DetallePedidoUpdate
from app.crud import crud_detalle_pedido
from app.database import SessionLocal

router = APIRouter(prefix="/detalle_pedido", tags=["detalle_pedido"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=DetallePedidoOut, status_code=status.HTTP_201_CREATED)
def crear_detalle_pedido(detalle: DetallePedidoCreate, db: Session = Depends(get_db)):
    return crud_detalle_pedido.crear_detalle_pedido(db, detalle)

@router.get("/", response_model=List[DetallePedidoOut])
def listar_detalles_pedido(db: Session = Depends(get_db)):
    return crud_detalle_pedido.obtener_detalles_pedido(db)

@router.get("/pedido/{pedido_id}", response_model=List[DetallePedidoOut])
def obtener_detalles_por_pedido(pedido_id: int, db: Session = Depends(get_db)):
    detalles = crud_detalle_pedido.obtener_detalles_por_pedido(db, pedido_id)
    if not detalles:
        raise HTTPException(status_code=404, detail="Detalles no encontrados para ese pedido")
    return detalles

@router.put("/{detalle_id}", response_model=DetallePedidoOut)
def actualizar_detalle_pedido(detalle_id: int, detalle_data: DetallePedidoUpdate, db: Session = Depends(get_db)):
    detalle = crud_detalle_pedido.actualizar_detalle_pedido(db, detalle_id, detalle_data)
    if not detalle:
        raise HTTPException(status_code=404, detail="Detalle no encontrado")
    return detalle

@router.delete("/{detalle_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_detalle_pedido(detalle_id: int, db: Session = Depends(get_db)):
    detalle = crud_detalle_pedido.eliminar_detalle_pedido(db, detalle_id)
    if not detalle:
        raise HTTPException(status_code=404, detail="Detalle no encontrado")