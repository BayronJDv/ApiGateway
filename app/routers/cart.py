from fastapi import APIRouter, Header, Body

router = APIRouter(
    prefix="/cart",
    tags=["Cart"]
)

@router.get("")
async def get_cart(
    authorization: str = Header(...)
):
    """
    USUARIO AUTENTICADO

    Este endpoint:
    - Recibe el JWT (Supabase)
    - El gateway valida el usuario
    - Reenvía la solicitud al microservicio de cart

    No recibe body

    Respuesta esperada desde el microservicio:
    [
        {
            "id": int,
            "product": {
                "id": int,
                "name": string,
                "price": float,
                "imageurl": string
            },
            "quantity": int
        },
        ...
    ]
    """
    pass

@router.post("/items")
async def add_to_cart(
    authorization: str = Header(...),
    body: dict = Body(...)
):
    """
    USUARIO AUTENTICADO

    Body esperado:
    {
        "product_id": int,
        "quantity": int (opcional, default = 1)
    }

    El gateway:
    - Valida JWT
    - Reenvía user_id + body al microservicio

    Respuesta esperada:
    {
        "message": "Product added to cart"
    }
    """
    pass

@router.delete("/items")
async def remove_from_cart(
    authorization: str = Header(...),
    body: dict = Body(...)
):
    """
    USUARIO AUTENTICADO

    Body esperado:
    {
        "product_id": int
    }

    El gateway:
    - Valida JWT
    - Reenvía user_id + product_id al microservicio

    Respuesta esperada:
    {
        "success": true
    }

    Si el item no existe:
    {
        "success": false,
        "message": "Item not found in cart"
    }
    """
    pass
