from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from supabase import create_client, Client
from dotenv import load_dotenv
import os

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()

supabase: Client = create_client(
    os.getenv("VITE_SUPABASE_URL"),
    os.getenv("VITE_SUPABASE_ANON_KEY")
)

@app.get("/orders")
async def ruta_protegida(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="No autorizado")
    
    # Extraer token (quitar "Bearer ")
    token = authorization.replace("Bearer ", "")
    
    try:
        user = supabase.auth.get_user(token)
        print(f"Usuario autenticado: {user}")
        return {"mensaje": "Acceso permitido", "usuario": user.user.email}
    except Exception as e:
        raise HTTPException(status_code=401, detail="Token inválido")