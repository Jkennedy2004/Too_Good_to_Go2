from sqlalchemy.orm import Session
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate, UsuarioUpdate

# Crear
def crear_usuario(db: Session, usuario: UsuarioCreate):
    nuevo_usuario = Usuario(**usuario.dict())
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

# Leer
def obtener_usuarios(db: Session):
    return db.query(Usuario).all()

def obtener_usuario_por_id(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()

# Actualizar
def actualizar_usuario(db: Session, usuario_id: int, usuario_data: UsuarioUpdate):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if usuario:
        for field, value in usuario_data.dict(exclude_unset=True).items():
            setattr(usuario, field, value)
        db.commit()
        db.refresh(usuario)
    return usuario

# Eliminar
def eliminar_usuario(db: Session, usuario_id: int):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if usuario:
        db.delete(usuario)
        db.commit()
    return usuario