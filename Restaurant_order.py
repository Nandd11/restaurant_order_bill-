class RestaurantOrderSystem:
    def __init__(self):
        self.menu = {
            '1': {'item': 'Burger', 'price': 120},
            '2': {'item': 'Pizza', 'price': 340},
            '3': {'item': 'Pasta', 'price': 180},
            '4': {'item': 'Salad', 'price': 220},
            '5': {'item': 'Soda', 'price': 120},
            '6': {'item': 'Water', 'price': 110},
            '7': {'item': 'Ice Cream', 'price': 140}
        }
        self.orders = []
        self.tax_rate = 0.05  # 5% tax
    
    def display_menu(self):
        print("\n===== MENU =====")
        for key, item in self.menu.items():
            print(f"{key}. {item['item']:15} ₹{item['price']:.2f}")
        print("8. Finish Order")
        print("================")
    
    def take_order(self):
        print("Welcome to our Restaurant!")
        print("Please select items from our menu:")
        
        while True:
            self.display_menu()
            choice = input("Enter item number (1-7) or 8 to finish: ")
            
            if choice == '8':
                if not self.orders:
                    print("You haven't ordered anything yet!")
                    continue
                break
            
            if choice in self.menu:
                quantity = input(f"How many {self.menu[choice]['item']}s would you like? ")
                try:
                    quantity = int(quantity)
                    if quantity > 0:
                        self.orders.append({
                            'item': self.menu[choice]['item'],
                            'price': self.menu[choice]['price'],
                            'quantity': quantity
                        })
                        print(f"Added {quantity} {self.menu[choice]['item']}(s) to your order.")
                    else:
                        print("Quantity must be at least 1.")
                except ValueError:
                    print("Please enter a valid number for quantity.")
            else:
                print("Invalid choice. Please select a valid item number.")
    
    def calculate_bill(self):
        subtotal = sum(item['price'] * item['quantity'] for item in self.orders)
        tax = subtotal * self.tax_rate
        total = subtotal + tax
        return subtotal, tax, total
    
    def print_bill(self):
        if not self.orders:
            print("No items ordered.")
            return
        
        print("\n===== FINAL BILL =====")
        print("{:<20} {:<10} {:<10} {:<10}".format("Item", "Price", "Qty", "Amount"))
        print("-" * 50)
        
        for item in self.orders:
            amount = item['price'] * item['quantity']
            print("{:<20} ₹{:<9.2f} {:<10} ₹{:<10.2f}".format(
                item['item'], item['price'], item['quantity'], amount))
        
        subtotal, tax, total = self.calculate_bill()
        
        print("\n{:<20} ₹{:<10.2f}".format("Subtotal:", subtotal))
        print("{:<20} ₹{:<10.2f}".format(f"Tax ({self.tax_rate*100:.0f}%):", tax))
        print("{:<20} ₹{:<10.2f}".format("Total:", total))
        print("=" * 25)
        print("Thank you for dining with us!")
        print("=" * 25)

# Main program
if __name__ == "__main__":
    system = RestaurantOrderSystem()
    system.take_order()
    system.print_bill()