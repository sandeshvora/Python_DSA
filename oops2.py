import csv
class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity: int = 0):
        # Run Validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"quantity {quantity} is not greater than or equal to zero"

        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        #Actions to Execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    # to print friendly display of values
    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"

    def apply_discount(self):
        return self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            print(item)

# for i in Item.all:
#     print(i)

Item.instantiate_from_csv()
