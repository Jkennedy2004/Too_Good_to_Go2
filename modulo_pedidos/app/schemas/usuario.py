from pydantic import BaseModel, EmailStr
from typing import Optional

class UsuarioBase(BaseModel):
    nombre: str
    correo: EmailStr

class UsuarioCreate(UsuarioBase):
    contrasena: str

class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    correo: Optional[EmailStr] = None
    contrasena: Optional[str] = None

class UsuarioOut(UsuarioBase):
    id: int

    class Config:
        orm_mode = True