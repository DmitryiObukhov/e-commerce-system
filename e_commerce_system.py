from CommerceClasses.user import User
from CommerceClasses.cart import ShoppingCart
from CommerceClasses.product import Product
from CommerceClasses.warehouse import Warehouse
from CommerceClasses.order import Order


warehouse = Warehouse()
apple = Product("Apple", "Fresh Red Apple", 0.5)
banana = Product("Banana", "Fresh Yellow Banana", 0.3)

warehouse.add_product(apple, 100)
warehouse.add_product(banana, 150)
print('Current number of products: ', warehouse.view_stock())

user = User("John Doe", "john.doe@example.com")
user.add_to_cart(apple, 5)
user.add_to_cart(banana, 10)
print('User products: ', user.view_cart())

order = Order(user, warehouse)
order.place_order()
print('Current number of products: ', warehouse.view_stock())
