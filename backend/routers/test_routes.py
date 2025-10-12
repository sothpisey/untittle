from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from db.base import fetch_products, Product, ProductCreate, insert_product
from security.token_handler import get_current_user

router = APIRouter(prefix='/api/tests', tags=['test_routes'])

@router.get('/products', response_model=list[Product])
def get_product_data(username: str = Depends(get_current_user)) -> list[Product]:
    products = fetch_products()
    if not products:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No products found')
    return products


@router.post('/products', status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate, username: str = Depends(get_current_user)):
    success = insert_product(product)
    if not success:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Failed to insert product')
    return {'detail': 'Product inserted successfully'}