from pydantic import BaseModel
from typing import Optional

class RestauranteBase(BaseModel):
    nombre: str
    direccion: str
    telefono: Optional[str] = None

class RestauranteCreate(RestauranteBase):
    pass

class RestauranteUpdate(BaseModel):
    nombre: Optional[str] = None
    direccion: Optional[str] = None
    telefono: Optional[str] = None

class RestauranteOut(RestauranteBase):
    id: int

    class Config:
        orm_mode = True