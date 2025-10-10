from fastapi import APIRouter, Depends, status, HTTPException
from db.base import fetch_products, Product
from security.token_handler import get_current_user

router = APIRouter(prefix='/api/tests', tags=['test_routes'])

@router.get('/products', response_model=list[Product])
def get_product_data(username: str = Depends(get_current_user)) -> list[Product]:
    products = fetch_products()
    if not products:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No products found')
    return products