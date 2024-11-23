class Product:
    total_products = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.increment_product_count()

    def __str__(self):
        return f'{self.name} {self.price}'

    @classmethod
    def increment_product_count(cls):
        cls.total_products += 1

    @classmethod
    def get_total_products(cls):
        """Returns the total number of products in the store."""
        return cls.total_products


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        """Adds a product to the cart."""
        self.items.append(product)

    def calculate_total(self):
        """Calculates the total price of items in the cart."""
        total_price = sum(product.price for product in self.items)
        return total_price

    def show_cart(self):
        print("Items in the box:")
        """Displays the items in the cart and their total price."""
        for product in self.items:
            print(f"- {product.name}: ${product.price}")
        print(f"Total price: ${self.calculate_total()}")


