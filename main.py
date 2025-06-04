from customer import Customer
from coffee import Coffee
from order import Order

# Create customers
alice = Customer("Alice")
bob = Customer("Bob")

# Create coffees
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# Create orders
Order(alice, latte, 4.5)
Order(alice, espresso, 3.0)
Order(bob, latte, 4.5)

# Test relationships and aggregates
print(f"Alice's total spent: ${alice.total_spent():.2f}")
print(f"Bob ordered coffees: {[coffee.name for coffee in bob.coffees()]}")
print(f"Customers who ordered Latte: {[c.name for c in latte.customers()]}")