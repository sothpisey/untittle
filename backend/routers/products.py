from fastapi import APIRouter, Depends, status, HTTPException
from security.token_handler import get_current_user
from db.base import (fetch_products, 
                     Product, 
                     ProductCreate, 
                     insert_product, 
                     fetch_product_by_id, 
                     update_product_in_db, 
                     delete_product_in_db,
                     ProductUpdate)


router = APIRouter(prefix='/api/v1/products', tags=['Products'])

@router.get('/', response_model=list[Product])
def get_product_data(username: str = Depends(get_current_user)) -> list[Product]:
    products = fetch_products()
    if not products:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No products found')
    return products


@router.get('/{product_id}', response_model=Product)
def get_product(product_id: int, username: str = Depends(get_current_user)) -> Product:
    product = fetch_product_by_id(product_id, is_username=False)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found')
    return product


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate, username: str = Depends(get_current_user)):
    success = insert_product(product)
    if not success:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Failed to insert product')
    return {'detail': 'Product inserted successfully'}


@router.put('/', status_code=status.HTTP_200_OK)
def update_product(product: Product, username: str = Depends(get_current_user)):
    success = update_product_in_db(product)
    if not success:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Failed to update product')
    return {'detail': 'Product updated successfully'}


@router.delete('/{product_id}', status_code=status.HTTP_200_OK)
def delete_product(product_id: int, username: str = Depends(get_current_user)):
    success = delete_product_in_db(product_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Failed to delete product')
    return {'detail': 'Product deleted successfully'}


@router.patch('/{product_id}', status_code=status.HTTP_200_OK)
def patch_product(product_id: int, product: ProductUpdate, username: str = Depends(get_current_user)):
    existing_product = fetch_product_by_id(product_id, is_username=False)
    if not existing_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found')

    updated_product = Product(
        id=existing_product.id,
        name=product.name if product.name is not None else existing_product.name,
        quantity=product.quantity if product.quantity is not None else existing_product.quantity,
        price=product.price if product.price is not None else existing_product.price,
        product_type=product.product_type if product.product_type is not None else existing_product.product_type
    )

    success = update_product_in_db(updated_product)
    if not success:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Failed to update product')
    return {'detail': 'Product updated successfully'}