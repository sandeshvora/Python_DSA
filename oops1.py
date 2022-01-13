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
item1 = Item("Phone", 80, 2)
item2 = Item("laptop", 1800, 5)
item1.pay_rate=0.6 # if want to assign specific discount to instance
# print(item1.name, item1.price, item1.price * item1.quantity)
# print()
# print(item1.calculate_total_price())
# print(item2.calculate_total_price())
#
# print(Item.pay_rate) # accessing class attribute directly
# print(item1.pay_rate) #accessing class attrubte thru instance and get it bcoz no pay_rate variable in instance item1
# print(Item.__dict__) # get all class level attributes
# print(item1.__dict__) # get all instance level attributes

print(item1.apply_discount())
print(Item.all)
