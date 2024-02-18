import json


class Category:
    """Класс категории"""
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str):
        """
        Инициализатор класса Category.
        name: Название категории.
        description: Описание категории.
        products: Список продуктов в данной категории.
        """
        self.name = name
        self.description = description
        self.products = []
        Category.total_categories += 1

    def count_unique_products(self):
        """Возвращает количество уникальных продуктов в данной категории."""
        return len(set(self.products))


class Product:
    """Классы продукт"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализатор класса Product.
        name: Название продукта.
        description: Описание продукта.
        price: Цена продукта.
        quantity: Количество продукта.
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        Category.total_products += 1


def load_data_from_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    categories = []
    for category_data in data:
        category = Category(category_data['name'], category_data['description'])
        for product_data in category_data['products']:
            product = Product(product_data['name'], product_data['description'], product_data['price'],
                              product_data['quantity'])
            category.products.append(product)
        categories.append(category)
    return categories


# Пример использования:
categories = load_data_from_json('products.json')

# Проверим результат
for category in categories:
    print(f"Категория: {category.name}")
    print(f"Описание: {category.description}")
    for product in category.products:
        print(
            f" - Товар: {product.name}, Описание: {product.description}, Цена: {product.price},"
            f"Количество: {product.quantity}")
    print()
