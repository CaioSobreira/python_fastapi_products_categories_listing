import pytest
from app.schemas.product import Product, ProductInput, ProductOutput
from app.schemas.category import Category

def test_product_schema():
    product = Product(
        name='Camisa Mike',
        slug='camisa-mike',
        price=20.99,
        stock=20
    )

    assert product.dict() == {
        'name': 'Camisa Mike',
        'slug': 'camisa-mike',
        'price': 20.99,
        'stock': 20
    }

def test_product_schema_invalid_slug():
    with pytest.raises(ValueError):
        product = Product(
            name='Camisa Mike',
            slug='camisa mike',
            price=20.99,
            stock=20
        )

    with pytest.raises(ValueError):
        product = Product(
            name='Camisa Mike',
            slug='cão',
            price=20.99,
            stock=20
        )

    with pytest.raises(ValueError):
        product = Product(
            name='Camisa Mike',
            slug='Camisa-mike',
            price=20.99,
            stock=20
        )

def test_product_schema_invalid_price():
    with pytest.raises(ValueError):
        product = Product(
            name='Camisa Mike',
            slug='camisa-mike',
            price=0,
            stock=20
        )

def test_product_input_schema():
    product = Product(
            name='Camisa Mike',
            slug='camisa-mike',
            price=20.99,
            stock=20
        )
    
    product_input = ProductInput(
        category_slug='roupa',
        product=product
    )

    assert product_input.dict() == {
        "category_slug": "roupa",
        "product" : {
            'name': 'Camisa Mike',
            'slug': 'camisa-mike',
            'price': 20.99,
            'stock': 20
        }
    }

def test_product_output_schema():
    category = Category(name='Roupa', slug='roupa')

    product_output = ProductOutput(
            id=1,
            name='Camisa',
            slug='camisa',
            price=10,
            stock=10,
            category=category
    )

    assert product_output.dict() == {
        'id': 1,
        'name': 'Camisa',
        'slug': 'camisa',
        'price': 10,
        'stock': 10,
        'category': {
            'name': 'Roupa',
            'slug': 'roupa'
        }
    }