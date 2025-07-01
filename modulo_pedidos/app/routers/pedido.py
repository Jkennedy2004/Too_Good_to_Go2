from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.pedido import PedidoCreate, PedidoOut, PedidoUpdate
from app.crud import crud_pedido
from app.database import SessionLocal

router = APIRouter(prefix="/pedidos", tags=["pedidos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=PedidoOut, status_code=status.HTTP_201_CREATED)
def crear_pedido(pedido: PedidoCreate, db: Session = Depends(get_db)):
    return crud_pedido.crear_pedido(db, pedido)

@router.get("/", response_model=List[PedidoOut])
def listar_pedidos(db: Session = Depends(get_db)):
    return crud_pedido.obtener_pedidos(db)

@router.get("/{pedido_id}", response_model=PedidoOut)
def obtener_pedido(pedido_id: int, db: Session = Depends(get_db)):
    pedido = crud_pedido.obtener_pedido_por_id(db, pedido_id)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return pedido

@router.put("/{pedido_id}", response_model=PedidoOut)
def actualizar_pedido(pedido_id: int, pedido_data: PedidoUpdate, db: Session = Depends(get_db)):
    pedido = crud_pedido.actualizar_pedido(db, pedido_id, pedido_data)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return pedido

@router.delete("/{pedido_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_pedido(pedido_id: int, db: Session = Depends(get_db)):
    pedido = crud_pedido.eliminar_pedido(db, pedido_id)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")