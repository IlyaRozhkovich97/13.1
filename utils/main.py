class Category:
    """Класс категории"""
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.products = ["Iphone 15 pro MAX", "1TB, Gray space", 14600, 10]
        Category.total_categories += 1


class Product:
    """Классы продукт"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        Category.total_products += 1


# Создаем экземпляр класса Category
category1 = Category("Смартфоны",
                     "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для "
                     "удобства"
                     "жизни")

# Создаем экземпляр класса Product
product1 = Product("Iphone 15 pro MAX", "1TB, Gray space", 14600, 10)
