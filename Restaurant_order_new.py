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
        print("9. Remove Item")
        print("================")
    
    def display_current_order(self):
        if not self.orders:
            print("\nYour order is currently empty.")
            return
        
        print("\n===== YOUR ORDER =====")
        print("{:<5} {:<20} {:<10} {:<10}".format("No.", "Item", "Price", "Qty"))
        print("-" * 45)
        for i, item in enumerate(self.orders, 1):
            print("{:<5} {:<20} ₹{:<9.2f} {:<10}".format(
                i, item['item'], item['price'], item['quantity']))
        print("=" * 45)
    
    def take_order(self):
        print("Welcome to our Restaurant!")
        print("Please select items from our menu:")
        
        while True:
            self.display_menu()
            self.display_current_order()
            
            choice = input("\nEnter item number (1-7), 8 to finish, or 9 to remove: ")
            
            if choice == '8':
                if not self.orders:
                    print("You haven't ordered anything yet!")
                    continue
                break
            
            elif choice == '9':
                self.remove_item()
            
            elif choice in self.menu:
                self.add_item(choice)
            
            else:
                print("Invalid choice. Please select a valid option.")
    
    def add_item(self, choice):
        quantity = input(f"How many {self.menu[choice]['item']}s would you like? ")
        try:
            quantity = int(quantity)
            if quantity > 0:
                # Check if item already exists in order
                existing_item = next((item for item in self.orders 
                                    if item['item'] == self.menu[choice]['item']), None)
                if existing_item:
                    existing_item['quantity'] += quantity
                    print(f"Added {quantity} more {self.menu[choice]['item']}(s) to your order.")
                else:
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
    
    def remove_item(self):
        if not self.orders:
            print("Your order is empty. Nothing to remove.")
            return
        
        self.display_current_order()
        try:
            item_num = input("Enter the item number you want to remove (or 0 to cancel): ")
            if item_num == '0':
                return
            
            item_num = int(item_num)
            if 1 <= item_num <= len(self.orders):
                item = self.orders[item_num-1]
                quantity = input(f"How many {item['item']}s do you want to remove (current: {item['quantity']})? ")
                quantity = int(quantity)
                
                if quantity <= 0:
                    print("Quantity must be at least 1.")
                elif quantity >= item['quantity']:
                    del self.orders[item_num-1]
                    print(f"Removed all {item['item']}(s) from your order.")
                else:
                    item['quantity'] -= quantity
                    print(f"Removed {quantity} {item['item']}(s) from your order.")
            else:
                print("Invalid item number.")
        except (ValueError, IndexError):
            print("Please enter a valid item number.")
    
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