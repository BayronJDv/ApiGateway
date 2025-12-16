from fastapi import HTTPException

from .config import supabase


# Funcion para verificar si el usuario esta autenticado
# devuelve el ide del usuario si esta autenticado
def is_authenticated(authorization):
    if not authorization:
        raise HTTPException(status_code=401, detail="No autorizado")

    # Extraer token (quitar "Bearer ")
    token = authorization.replace("Bearer ", "")

    try:
        user = supabase.auth.get_user(token)
        return user.user.id
    except Exception as e:
        raise HTTPException(status_code=401, detail="Token inválido")
