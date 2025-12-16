from fastapi import FastAPI, Header, HTTPException
from supabase_auth.types import User

from app.core.Auth import is_authenticated
from app.core.config import supabase
from app.core.cors import setup_cors
from app.routers import admin_products, cart, products

app = FastAPI(title="API Gateway")

# CORS
setup_cors(app)

# Routers
app.include_router(products.router)
app.include_router(admin_products.router)
app.include_router(cart.router)


@app.get("/example")
async def ruta_protegida(authorization: str = Header(None)):
    Userid = is_authenticated(authorization)
    if not Userid:
        raise HTTPException(status_code=401, detail="No autorizado")
    else:
        return {"mensaje": "Acceso permitido", "usuario": Userid}
