from fastapi import APIRouter

# establecer el endpoint por defecto,también agrupa el router en la documentacion
router = APIRouter(prefix="/products",
                   tags=["products"],
                   responses={404: {"message": "No encontrado"}})


products_list = ["Producto 1", "Producto 2",
                 "Producto 3", "Producto 4", "Producto 5"]


@router.get("/")
async def products():  # type: ignore
    return products_list


@router.get("/{id}")
async def products(id: int):
    return products_list[id]
