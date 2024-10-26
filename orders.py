class Order:
    order_count = 0

    def __init__(self):
        self.products = []
        Order.order_count += 1

    def add_product(self, product):
        self.products.append(product)

    def total_price(self):
        return sum(product.price for product in self.products)

    @classmethod
    def total_orders(cls):
        return cls.order_count

    def __str__(self):
        return f"Order(total items: {len(self.products)}, total price: {self.total_price():.2f})"

    def __repr__(self):
        return f"Order({self.products})"
