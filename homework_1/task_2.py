import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
logger = logging.getLogger()

class Product:
    def __init__(self, name, quantity, price):
        self.name = name  # Название продукта
        self.quantity = quantity  # Количество на складе
        self.price = price    # Стоимость единицы

    def increase_stock(self, amount):
        self.quantity += amount

    def decrease_stock(self, amount):
        if amount > self.quantity:
            raise ValueError(f"Недостаточно товара '{self.name}' на складе.")
        self.quantity -= amount

    def calculate_total_value(self):
        return self.quantity * self.price

class Warehouse:
    def __init__(self):
        self.products = {}  # Словарь для хранения продуктов

    def add_product(self, product: Product):
        if product.name in self.products:
            self.products[product.name].increase_stock(product.quantity)
        else:
            self.products[product.name] = product
        logger.info(f"Добавлено {product.name} в количестве {product.quantity}")

    def remove_product(self, product_name):
        if product_name in self.products:
            del self.products[product_name]
        else:
            raise ValueError(f"Продукт '{product_name}' отсутствует на складе.")

    def calculate_total_inventory_value(self):
        total_value = sum(product.calculate_total_value() for product in self.products.values())
        logger.info(f"Общая стоимость продуктов на складе: {total_value} руб.")
        return total_value

class Seller:
    def __init__(self, seller_name):
        self.seller_name = seller_name
        self.sales_history = []
        self.total_sales = 0

    def sell_product(self, warehouse, product_name, amount):
        if product_name not in warehouse.products:
            raise ValueError(f"Продукт '{product_name}' отсутствует на складе.")
        
        product = warehouse.products[product_name]
        product.decrease_stock(amount)
        revenue = product.price * amount
        self.sales_history.append({"name": product_name, "amount": amount, "revenue": revenue})
        self.total_sales += revenue
        
        if product.quantity == 0:
            warehouse.remove_product(product_name)
            logger.info(f"Продукт {product.name} удалён из склада")
        
        logger.info(f"Продажа {amount} единиц продукта {product_name}")

    def generate_sales_report(self):
        report_lines = [f"{sale['amount']} x {sale['name']} = {sale['revenue']} руб." for sale in self.sales_history]
        report = "\n".join(report_lines) + f"\nОбщая выручка: {self.total_sales} руб."
        logger.info(f"Отчёт о продажах:\n{report}")
        return report

if __name__ == "__main__":
    # Пример работы системы
    warehouse = Warehouse()
    seller = Seller(seller_name="Владимир")

    # Добавление продуктов на склад
    warehouse.add_product(Product(name="Бананы", quantity=40, price=100))
    warehouse.add_product(Product(name="Апельсины", quantity=60, price=150))
    warehouse.add_product(Product(name="Яблоки", quantity=100, price=80))

    # Продажа продуктов
    seller.sell_product(warehouse, "Бананы", 20)
    seller.sell_product(warehouse, "Апельсины", 50)
    seller.sell_product(warehouse, "Яблоки", 20)

    # Генерация отчёта о продажах
    sales_report = seller.generate_sales_report()

    # Вывод общей стоимости оставшихся продуктов
    remaining_value = warehouse.calculate_total_inventory_value()
