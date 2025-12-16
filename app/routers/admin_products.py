from fastapi import APIRouter, Header, Path

router = APIRouter(
    prefix="/admin/products",
    tags=["Admin Products"]
)

@router.get("")
async def admin_get_products(
    authorization: str = Header(...)
):
    """
    SOLO ADMIN

    Devuelve:
    - Lista completa de productos
    """
    pass


@router.get("/{product_id}")
async def admin_get_product(
    product_id: int = Path(...),
    authorization: str = Header(...)
):
    """
    SOLO ADMIN

    Devuelve:
    - Producto específico
    """
    pass


@router.post("")
async def admin_create_product(
    authorization: str = Header(...)
):
    """
    SOLO ADMIN

    Body:
    - Datos del producto

    Devuelve:
    - Producto creado
    """
    pass


@router.put("/{product_id}")
async def admin_update_product(
    product_id: int = Path(...),
    authorization: str = Header(...)
):
    """
    SOLO ADMIN

    Body:
    - Campos parciales del producto

    Devuelve:
    - Producto actualizado
    """
    pass


@router.delete("/{product_id}")
async def admin_delete_product(
    product_id: int = Path(...),
    authorization: str = Header(...)
):
    """
    SOLO ADMIN

    Devuelve:
    - Mensaje de confirmación
    """
    pass
