##Flower Shop Ordering To Go Project 

class Flower:
    def __init__(self, name, color, price, quantity):
        self.name = name
        self.color = color
        self.price = price
        self.quantity = quantity

    def display_flower(self):
        print(f"{self.name} ({self.color}): {self.price} - {self.quantity} in stock")

class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def display_bouquet(self):
        total_price = 0
        for flower in self.flowers:
            flower.display_flower()
            total_price += flower.price
        print(f"Total price: {total_price}")

class FlowerShop:
    def __init__(self):
        self.inventory = {}
        self.orders = []

    def add_flower(self, flower):
        if flower.name in self.inventory:
            self.inventory[flower.name].quantity += flower.quantity
        else:
            self.inventory[flower.name] = flower

    def create_bouquet(self, flowers):
        bouquet = Bouquet()
        for flower in flowers:
            if self.inventory[flower.name].quantity == 0:
                print(f"{flower.name} is out of stock")
                return None
            else:
                bouquet.add_flower(flower)
                self.inventory[flower.name].quantity -= 1
        return bouquet

    def display_inventory(self):
        print("\nFlower Inventory:")
        for flower in self.inventory.values():
            flower.display_flower()

    def take_order(self, bouquet):
        if bouquet:
            self.orders.append(bouquet)

    def display_orders(self):
        print("\nOrders:")
        for idx, order in enumerate(self.orders, start=1):
            print(f"Order {idx}:")
            order.display_bouquet()
            print("----------")

# Sample usage
shop = FlowerShop()
shop.add_flower(Flower("Rose", "Red", 2.99, 10))
shop.add_flower(Flower("Rose", "White", 2.99, 5))
shop.add_flower(Flower("Lily", "Yellow", 3.99, 7))
shop.add_flower(Flower("Tulip", "Pink", 1.99, 3))

while True:
    print("\nOptions:")
    print("1. Display Flower Inventory")
    print("2. Create Bouquet and Place Order")
    print("3. Display Orders")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        shop.display_inventory()
    elif choice == "2":
        flower_names = input("Enter flower names for the bouquet (comma-separated): ").split(",")
        bouquet_flowers = []
        for name in flower_names:
            name = name.strip()
            if name in shop.inventory:
                quantity = int(input(f"Enter the quantity of {name}: "))
                if quantity > shop.inventory[name].quantity:
                    print(f"Not enough {name} in stock")
                else:
                    bouquet_flowers.extend([shop.inventory[name]] * quantity)
            else:
                print(f"{name} is not in the inventory.")
                break
        else:
            bouquet = shop.create_bouquet(bouquet_flowers)
            if bouquet:
                shop.take_order(bouquet)
                print("Bouquet created and order placed.")
    elif choice == "3":
        shop.display_orders()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please choose again.")
