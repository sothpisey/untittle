from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from db.base import fetch_products
from security.token_handler import get_current_user

router = APIRouter(prefix='/api')

@router.get('/products')
def get_product_data(username: str = Depends(get_current_user)) -> JSONResponse:
    products = fetch_products()
    if products:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"products": [product.dict() for product in products]})
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"error": "No products found"})