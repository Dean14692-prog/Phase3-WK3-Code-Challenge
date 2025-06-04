class Coffee:
    
    all_coffees = []

    def __init__(self, name):
        self.name = name
        Coffee.all_coffees.append(self)

    def orders(self):
        from order import Order
        return [order for order in Order.all_orders if order.coffee == self]

    def customers(self):
        return list({order.customer for order in self.orders()})