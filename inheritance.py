# Task 1
class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity


class Book(Product):
    def __init__(self, name: str, price: float, quantity: int, author: str):
        super().__init__(name, price, quantity)
        self.author = author

    def read(self):
        pass


# Task 2
class Restaurant:
    def __init__(self, name: str, cuisine: str, menu: dict):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu


class FastFood(Restaurant):
    def __init__(self, name: str, cuisine: str, menu: dict, drive_thru: bool):
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru

    def order(self, dish_name: str, quantity: int):
        if dish_name not in self.menu:
            return 'Dish not available'
        if self.menu[dish_name]['quantity'] >= quantity:
            self.menu[dish_name]['quantity'] -= quantity
            return self.menu[dish_name]['price'] * quantity
        else:
            return 'Requested quantity not available'

