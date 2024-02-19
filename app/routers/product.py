import db_on_mem
from fastapi import APIRouter
from schema import Product

router = APIRouter()


@router.get('/product')
def get_products():
    return db_on_mem.db_products.get_products()

@router.post('/product')
def create_product(product: Product):
    return db_on_mem.db_products.add_product(product)