class Product:
    def __init__(self, name, price, quantity, category):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__category = category

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, value):
        self.__category = value

    def calculate_total(self):
        total = self.__price * self.__quantity
        return total
    
    def __str__(self):
        return f"Name: {self.name} | Price: {self.price} | Quantity: {self.quantity} | Category: {self.category}"
    
class PerishableProduct(Product):
    def __init__(self, name, price, quantity, category, expiration_date):
        super().__init__(name, price, quantity, category)
        self.__expiration_date = expiration_date

    @property
    def expiration_date(self):
        return self.__expiration_date

    @expiration_date.setter
    def expiration_date(self, value):
        self.__expiration_date = value

    def __str__(self):
        return super().__str__() + f" | Expiration Date: {self.__expiration_date}"