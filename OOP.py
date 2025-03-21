class Item:
    def __init__(self, name, price, quantity):
        print("Item created")
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def calculate_total_price(self):
        return print(self.price * self.quantity)
    
    
item1 = Item("Apple", 1.99, 10)
item2 = Item("Banana", 0.99, 5)
item3 = Item("Phone", 999.99, 10)

item1.calculate_total_price()
item2.calculate_total_price() 
item3.calculate_total_price()