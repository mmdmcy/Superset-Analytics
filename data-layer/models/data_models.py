class DataModel:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

class User(DataModel):
    def __init__(self, id, name, email):
        super().__init__(id, name, "User model")
        self.email = email

class Product(DataModel):
    def __init__(self, id, name, price):
        super().__init__(id, name, "Product model")
        self.price = price

class Sales(DataModel):
    def __init__(self, id, product_id, user_id, amount):
        super().__init__(id, "Sales Record", "Sales model")
        self.product_id = product_id
        self.user_id = user_id
        self.amount = amount

def get_all_models():
    return [User, Product, Sales]