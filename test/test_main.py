from utils.main import Category, Product


def test_category_initialization():
    category = Category("Смартфоны",
                        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для "
                        "удобства жизни")
    assert category.name == "Смартфоны"
    assert category.description == ("Смартфоны, как средство не только коммуникации, но и получение дополнительных "
                                    "функций для удобства жизни")
    assert category.products == ["Iphone 15 pro MAX", "1TB, Gray space", 14600, 10]


def test_product_initialization():
    product = Product("Iphone 15 pro MAX", "1TB, Gray space", 14600, 10)
    assert product.name == "Iphone 15 pro MAX"
    assert product.description == "1TB, Gray space"
    assert product.price == 14600
    assert product.quantity == 10


