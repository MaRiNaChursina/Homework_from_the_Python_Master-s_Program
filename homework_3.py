'''1. Класс Product

Атрибуты:
-name (строка) — название товара;
-price (число) — цена товара;
-stock (целое число) — количество товара на складе.
Методы:
-update_stock(quantity) — метод, который обновляет количество товара на складе. Если количество становится отрицательным, должно выдаваться сообщение об ошибке.
2. Класс Order

Атрибуты:
-products (словарь) — словарь, где ключом является объект Product, а значением — количество этого товара в заказе.
Методы:
-add_product(product, quantity) — метод для добавления товара в заказ. Если товара недостаточно на складе, должно выдаваться сообщение об ошибке;
-calculate_total() — метод для расчёта общей стоимости заказа.
3. Класс Store

Атрибуты:
-products (список) — список всех доступных товаров в магазине.
Методы:
-add_product(product) — метод для добавления товара в магазин;
-list_products() — метод для отображения всех товаров в магазине с их ценами и количеством на складе;
-create_order() — метод для создания нового заказа.
Сверьтесь с примером использования.

Дополнительные задания (выполняется по желанию)

1. Реализуйте возможность удаления товаров из заказа.
-Добавьте метод remove_product(product, quantity) в класс Order, который будет удалять указанное количество товара из заказа. Если количество товара в заказе становится равным нулю, удалите товар из словаря products.
2. Добавьте функциональность для обработки возвратов товаров и обновления запасов.
-Реализуйте метод return_product(product, quantity) в классе Order, который будет возвращать указанный товар обратно в магазин. Этот метод должен:

уменьшать количество товара в заказе;
вызывать метод update_stock(quantity) у объекта Product, чтобы увеличить количество товара на складе;
если количество товара в заказе становится равным нулю, удалите товар из словаря products.'''


class Product:
    def __init__ (self,name, price, stock ):
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        if self.stock < quantity:
            print(f'На складе нехватает товара {self.name}')
        else:
            self.stock += quantity

class Order:
    def __init__(self):
        self.products = {}

    def add_product(self, product, quantity):
        if product.stock < quantity:
            print(f'На складе меньше товара {product.name}')
            return
        else:
            self.products[product] = quantity
            product.update_stock(-quantity)

    def calculate_total(self):
        return sum(product.price * qty for product, qty in self.products.items())

    def remove_product(self, product, quantity):
        if self.products[product] > quantity:
            self.products[product] -= quantity
        else:
            del self.products[product]
            return

    def return_product(self, product, quantity):
        if self.products[product] > quantity:
            self.products[product] -= quantity
            product.update_stock(quantity)
        else:
            product.update_stock(self.products[product])
            del self.products[product]
            return
        


    def list_productss(self):
        for element in self.products:
            print(element.name)



class Store:
    def __init__(self):
        self.products = []

    def add_product(self,product):
        self.products.append(product)

    def list_products(self):
        for element in self.products:
            print(element.name, element.price, element.stock)
            
    def create_order(self):
        return Order()





if __name__ == "__main__":
    # Создаем магазин
    store = Store()

    # Создаем товары
    product1 = Product("Ноутбук", 1000, 5)
    product2 = Product("Смартфон", 500, 10)


    # Добавляем товары в магазин
    store.add_product(product1)
    store.add_product(product2)

    # Список всех товаров
    store.list_products()

    # Создаем заказ
    order = store.create_order()

    # Добавляем товары в заказ
    order.add_product(product1, 10)
    order.add_product(product2, 3)

    # Выводим общую стоимость заказа
    total = order.calculate_total()
    print(f"Общая стоимость заказа: {total}")

    # Проверяем остатки на складе после заказа
    store.list_products()