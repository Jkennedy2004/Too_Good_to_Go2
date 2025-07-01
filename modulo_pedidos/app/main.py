from fastapi import FastAPI
from app.database import engine, Base
from app.routes import usuario, restaurante, producto, pedido, detalle_pedido

# Crear tablas en la base de datos (si no existen)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Too Good To Go - API",
    description="API para la plataforma de comida no vendida con microservicios en FastAPI y PostgreSQL",
    version="1.0.0"
)

# Registrar routers
app.include_router(usuario.router)
app.include_router(restaurante.router)
app.include_router(producto.router)
app.include_router(pedido.router)
app.include_router(detalle_pedido.router)

# Ruta raíz para comprobar que la API está activa
@app.get("/")
def root():
    return {"message": "API Too Good To Go está activa"}