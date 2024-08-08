from CommerceClasses.cart import ShoppingCart


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cart = ShoppingCart()

    def add_to_cart(self, product, quantity):
        self.cart.add_item(product, quantity)

    def view_cart(self):
        return self.cart.view_items()
