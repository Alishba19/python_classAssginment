class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"

class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.items = []
        self.completed = False

    def add_item(self, menu_item, quantity=1):
        self.items.append((menu_item, quantity))

    def total_price(self):
        return sum(item.price * qty for item, qty in self.items)

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        item_lines = [f"{item.name} x{qty} - ${item.price * qty:.2f}" for item, qty in self.items]
        items_str = "\n  ".join(item_lines)
        return f"Order #{self.order_id} [{status}]\n  {items_str}\nTotal: ${self.total_price():.2f}"

class Restaurant:
    def __init__(self):
        self.menu = []
        self.orders = []
        self.next_order_id = 1

    def add_menu_item(self, name, price):
        self.menu.append(MenuItem(name, price))

    def show_menu(self):
        print("\n--- Menu ---")
        for idx, item in enumerate(self.menu, 1):
            print(f"{idx}. {item}")

    def create_order(self):
        order = Order(self.next_order_id)
        self.next_order_id += 1

        while True:
            self.show_menu()
            choice = input("Enter menu item number to add to order (or 'done' to finish): ").strip()
            if choice.lower() == "done":
                break
            if not choice.isdigit() or int(choice) < 1 or int(choice) > len(self.menu):
                print("Invalid choice, try again.")
                continue
            menu_item = self.menu[int(choice)-1]
            qty_input = input(f"Enter quantity for {menu_item.name}: ")
            if not qty_input.isdigit() or int(qty_input) < 1:
                print("Invalid quantity, try again.")
                continue
            quantity = int(qty_input)
            order.add_item(menu_item, quantity)
            print(f"Added {quantity} x {menu_item.name} to order.")

        if order.items:
            self.orders.append(order)
            print(f"\nOrder #{order.order_id} created successfully!")
        else:
            print("Order is empty, nothing added.")

    def list_orders(self):
        if not self.orders:
            print("No orders yet.")
            return
        print("\n--- Orders ---")
        for order in self.orders:
            print(order)
            print("-" * 20)

    def complete_order(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                if order.completed:
                    print(f"Order #{order_id} is already completed.")
                else:
                    order.mark_completed()
                    print(f"Order #{order_id} marked as completed.")
                return
        print(f"No order found with ID {order_id}.")

def main():
    restaurant = Restaurant()

    # Pre-populate menu
    restaurant.add_menu_item("Burger", 5.99)
    restaurant.add_menu_item("Pizza", 8.99)
    restaurant.add_menu_item("Salad", 4.50)
    restaurant.add_menu_item("Soda", 1.99)

    print("Welcome to the Restaurant Order Management System!")

    while True:
        print("\nOptions:")
        print("1. Show Menu")
        print("2. Create New Order")
        print("3. List All Orders")
        print("4. Complete an Order")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            restaurant.show_menu()
        elif choice == "2":
            restaurant.create_order()
        elif choice == "3":
            restaurant.list_orders()
        elif choice == "4":
            try:
                order_id = int(input("Enter Order ID to complete: "))
                restaurant.complete_order(order_id)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            print("Thank you! Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
