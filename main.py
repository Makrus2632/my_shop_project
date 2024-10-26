from products import Product
from customer_class import Customer
from orders import Order
from discounts import Discount

# Создание продуктов
product1 = Product('Laptop', 1200.99)
product2 = Product('Mouse', 25.50)
product3 = Product('Keyboard', 75.99)

# Создание клиентов
customer1 = Customer('John Doe')
customer2 = Customer('Jane Smith')

# Создание заказов и добавление продуктов
order1 = Order()
order1.add_product(product1)
order1.add_product(product2)

order2 = Order()
order2.add_product(product3)

# Добавление заказов клиентам
customer1.add_order(order1)
customer2.add_order(order2)

# Применение скидок
seasonal_discount = Discount("Seasonal Discount", 10)
promo_discount = Discount("Promo Code Discount", 15)

discounted_price1 = seasonal_discount.apply_seasonal_discount(order1, 10)
discounted_price2 = promo_discount.apply_promo_code(order2, 15)

# Подсчет общего количества заказов и суммы всех заказов
total_orders = Order.total_orders()
total_spent_by_customers = customer1.total_spent() + customer2.total_spent()

# Вывод информации
print(f"Количество всех заказов: {total_orders}")
print(f"Общая сумма всех заказов: {total_spent_by_customers:.2f}")
print(f"Сезонная скидка на первый заказ: {discounted_price1:.2f}")
print(f"Скидка по промокоду на второй заказ: {discounted_price2:.2f}")