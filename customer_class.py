class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def total_spent(self):
        return sum(order.total_price() for order in self.orders)

    def __str__(self):
        return f"Customer(name: {self.name}, total orders: {len(self.orders)})"

    def __repr__(self):
        return f"Customer('{self.name}')"
