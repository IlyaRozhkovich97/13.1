import pytest
from utils.main import Category, Product


@pytest.fixture
def reset_totals():
    Category.total_categories = 0
    Product.total_products = 0


def test_category_initialization(reset_totals):
    category = Category("Смартфоны",
                        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для "
                        "удобства жизни")
    assert category.name == "Смартфоны"
    assert category.description == ("Смартфоны, как средство не только коммуникации, но и получение дополнительных "
                                    "функций для удобства жизни")
    assert category.products == []
    assert Category.total_categories == 1


def test_product_initialization(reset_totals):
    product = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert product.name == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5
    assert Product.total_products == 1
