class Product:
    """
    Product class that contains the name, qty, and price of a product
    """

    def __init__(self, name, qty, price):
        self.name = name
        self.qty = qty
        self.price = price

    def update_price(self, price):
        self.price = price

    def add_qty(self, qty):
        self.qty += qty

    def remove_qty(self, qty):
        if qty > self.qty:
            raise Exception("Insufficient Quantity")
        else:
            self.qty -= qty

    def print_product(self):
        print ('{0} items of {1} priced at {2} each').format(self.qty,
                self.name, self.price)


class Inventory:

    def __init__(self,name):
        self.name = name
        self.products = []

    def add_product(self, Product):
        self.products.append(Product)

    def print_inventory(self):
        print self.name
        for pr in self.products:
            pr.print_product()

    def value(self):
        sum = 0
        for pr in self.products:
            sum += pr.qty * pr.price

        print ('Inventory Value = {0}').format(sum)




"""Testing Script"""
inv = Inventory('myInventory')
inv.add_product(Product("shampoo", 12, 10.04))
inv.add_product(Product('tel', 6, 8.07))
inv.print_inventory()
inv.value()

