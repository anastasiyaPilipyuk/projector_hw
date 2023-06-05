from account_class import Account


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
        return f"Book {self.name} by {self.author} was read"


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


# Task 3
class SavingsAccount(Account):
    def __init__(self, balance, account_number, interest):
        super().__init__(balance, account_number)
        self._interest = interest

    @classmethod
    def create_account(cls, account_number, interest):
        return cls(0.0, account_number, interest)

    def get_interest(self):
        return self._interest

    def add_interest(self):
        self._balance = self._balance + round((self._balance * self._interest) / 100, 2)


class CurrentAccount(Account):
    def __init__(self, balance, account_number, overdraft_limit):
        super().__init__(balance, account_number)
        self._overdraft_limit = overdraft_limit

    @classmethod
    def create_account(cls, account_number, overdraft_limit):
        return cls(0.0, account_number, overdraft_limit)

    def get_overdraft_limit(self):
        return self._overdraft_limit


class Bank:
    def __init__(self, name: str, accounts: list[Account] = []):
        self.name = name
        self._accounts = accounts

    def get_bank_accounts(self):
        return self._accounts

    # open account
    def open_account(self, account: Account):
        self._accounts.append(account)

    # add list of new accounts
    def open_accounts(self, accounts: list[Account]):
        self._accounts.extend(accounts)

    # close account by number
    def close_account(self, account_number):
        self._accounts = list(
            filter(lambda item: item.get_account_number() != account_number, self._accounts)
        )

    def pay_dividend(self, dividend):
        for account in self._accounts:
            account.deposit(dividend)

    def update(self):
        for account in self._accounts:
            if isinstance(account, SavingsAccount):
                account.add_interest()
            if isinstance(account, CurrentAccount) and account.get_balance() < account.get_overdraft_limit():
                print(f"Your account by number {account.get_account_number()}: is overdraft.")


