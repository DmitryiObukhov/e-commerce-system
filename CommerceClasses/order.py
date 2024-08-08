class Order:
    def __init__(self, user, warehouse):
        self.user = user
        self.warehouse = warehouse

    def place_order(self):
        for product, quantity in self.user.cart.items.items():
            if product in self.warehouse.products and self.warehouse.products[product] >= quantity:
                self.warehouse.products[product] -= quantity
            else:
                print(f"Insufficient stock for {product.name}")
