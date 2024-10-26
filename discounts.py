class Discount:
    def __init__(self, description, discount_percent):
        self.description = description
        self.discount_percent = discount_percent

    @staticmethod
    def apply_discount(price, discount_percent):
        return price * (1 - discount_percent / 100)

    @classmethod
    def apply_seasonal_discount(cls, order, discount_percent):
        total_price = order.total_price()
        return cls.apply_discount(total_price, discount_percent)

    @classmethod
    def apply_promo_code(cls, order, discount_percent):
        return cls.apply_seasonal_discount(order, discount_percent)

    def __str__(self):
        return f"Discount(description: {self.description}, discount_percent: {self.discount_percent}%)"

    def __repr__(self):
        return f"Discount('{self.description}', {self.discount_percent})"
