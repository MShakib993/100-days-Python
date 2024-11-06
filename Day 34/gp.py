# Function to initiate the process by asking the user type (seller or buyer)
def initiate():
    user_type = input("Press 'p' for seller and 'c' for buyer: ")

    if user_type == "p":
        add_inventory()  # Go to seller (add inventory) function
    elif user_type == "c":
        shop()  # Go to buyer (shopping) function
    else:
        print("Please press a valid button.")

# Function to initialize inventory quantities to zero
def initialize_inventory():
    global inventory_lower
    global inventory_shirt
    global inventory_tshirt
    inventory_lower = 0  # Inventory of lowers
    inventory_shirt = 0  # Inventory of shirts
    inventory_tshirt = 0  # Inventory of tshirts

# Function to initialize the cart quantities to zero
def initialize_cart():
    global cart_lower
    global cart_shirt
    global cart_tshirt
    cart_lower = 0  # Number of lowers in cart
    cart_shirt = 0  # Number of shirts in cart
    cart_tshirt = 0  # Number of tshirts in cart

# Function to display current cart items
def view_cart():
    global cart_lower
    global cart_shirt
    global cart_tshirt

    print("Lower = ", cart_lower)
    print("Shirt = ", cart_shirt)
    print("Tshirt = ", cart_tshirt)

# Function to initialize order quantities to zero
def initialize_orders():
    global order_lower
    global order_shirt
    global order_tshirt
    order_lower = 0  # Ordered lowers
    order_shirt = 0  # Ordered shirts
    order_tshirt = 0  # Ordered tshirts

# Function for seller to add products to inventory
def add_inventory():
    global inventory_lower
    global inventory_shirt
    global inventory_tshirt

    # Prompt seller to choose product type or check inventory
    item_type = input("Add item: Press 'l' for lower, 's' for shirt, 't' for tshirt, 'z' to view inventory: ")

    if item_type == "l":
        quantity = int(input("Enter number of lowers to add: "))
        inventory_lower += quantity
        print("Total lowers =", inventory_lower)  # Display updated inventory
    elif item_type == "s":
        quantity = int(input("Enter number of shirts to add: "))
        inventory_shirt += quantity
        print("Total shirts =", inventory_shirt)  # Display updated inventory
    elif item_type == "t":
        quantity = int(input("Enter number of tshirts to add: "))
        inventory_tshirt += quantity
        print("Total tshirts =", inventory_tshirt)  # Display updated inventory
    elif item_type == "z":
        # Show the current inventory
        print("Lowers =", inventory_lower)
        print("Shirts =", inventory_shirt)
        print("Tshirts =", inventory_tshirt)
    else:
        print("Invalid input")

# Function for buyer to shop and manage cart
def shop():
    global inventory_lower
    global inventory_shirt
    global inventory_tshirt

    global cart_lower
    global cart_shirt
    global cart_tshirt

    global order_lower
    global order_shirt
    global order_tshirt

    # Prompt buyer to choose product type, check out, or view orders
    item_type = input("Add to cart: Press 'l' for lower, 's' for shirt, 't' for tshirt, 'b' to buy, 'o' for orders: ")

    if item_type == "l":
        quantity = int(input("Enter number of lowers to buy: "))
        # Check if enough items are in inventory
        if quantity > inventory_lower:
            print(f"{quantity} lowers are not available.")
        else:
            inventory_lower -= quantity  # Update inventory
            print(f"{quantity} lowers added to your cart.")
            cart_lower += quantity  # Update cart
            if input("Enter 'c' to view cart or any key to continue: ") == "c":
                view_cart()  # Display cart if user chooses

    elif item_type == "s":
        quantity = int(input("Enter number of shirts to buy: "))
        if quantity > inventory_shirt:
            print(f"{quantity} shirts are not available.")
        else:
            inventory_shirt -= quantity
            print(f"{quantity} shirts added to your cart.")
            cart_shirt += quantity
            if input("Enter 'c' to view cart or any key to continue: ") == "c":
                view_cart()

    elif item_type == "t":
        quantity = int(input("Enter number of tshirts to buy: "))
        if quantity > inventory_tshirt:
            print(f"{quantity} tshirts are not available.")
        else:
            inventory_tshirt -= quantity
            print(f"{quantity} tshirts added to your cart.")
            cart_tshirt += quantity
            if input("Enter 'c' to view cart or any key to continue: ") == "c":
                view_cart()

    elif item_type == "b":
        # Finalize purchase and confirm payment
        view_cart()
        if input("Press 'a' to confirm purchase or any key to cancel: ") == "a":
            # Check if cart is empty before proceeding
            if cart_lower == 0 and cart_shirt == 0 and cart_tshirt == 0:
                print("Add items to your cart before buying.")
            else:
                # Collect personal details for delivery
                print("Personal details:")
                address = input("Enter your address: ")
                phone = input("Enter your phone number: ")
                payment = input("Enter 'cod' for cash on delivery or 'online' for online payment: ")

                if payment == "cod":
                    print("Order placed. It will arrive in 5 days.")
                    print("Thank you for your purchase!")
                elif payment == "online":
                    print("UPI ID: 8008978278. Please pay to complete the order.")
                    print("Thank you for your purchase!")

                # Move items from cart to order and reset cart
                order_lower, order_shirt, order_tshirt = cart_lower, cart_shirt, cart_tshirt
                cart_lower = cart_shirt = cart_tshirt = 0

    elif item_type == "o":
        # Display user's order history
        print("Lowers in order =", order_lower)
        print("Shirts in order =", order_shirt)
        print("Tshirts in order =", order_tshirt)
    else:
        print("Invalid input")

# Initialize all quantities to start fresh
initialize_orders()  # Set initial order values
initialize_inventory()  # Set initial inventory values
initialize_cart()  # Set initial cart values
initiate()  # Start the program by asking user type (seller or buyer)

# Allow user to continue shopping or exit
while input("Press 0 to continue shopping or any key to exit: ") == "0":
    initiate()  # Restart process for each round of shopping
else:
    print("Exited")  # Exit message when loop is broken
