def initiate():
    user_type = input("Press 'p' for seller and 'c' for buyer: ")

    if user_type == "p":
        add_inventory()
    elif user_type == "c":
        shop()
    else:
        print("Please press a valid button.")


def initialize_inventory():
    global inventory_lower
    global inventory_shirt
    global inventory_tshirt
    inventory_lower = 0
    inventory_shirt = 0
    inventory_tshirt = 0


def initialize_cart():
    global cart_lower
    global cart_shirt
    global cart_tshirt
    cart_lower = 0
    cart_shirt = 0
    cart_tshirt = 0


def view_cart():
    global cart_lower
    global cart_shirt
    global cart_tshirt

    print("Lower = ", cart_lower)
    print("Shirt = ", cart_shirt)
    print("Tshirt = ", cart_tshirt)


def initialize_orders():
    global order_lower
    global order_shirt
    global order_tshirt
    order_lower = 0
    order_shirt = 0
    order_tshirt = 0


def add_inventory():
    global inventory_lower
    global inventory_shirt
    global inventory_tshirt

    item_type = input("Add item: Press 'l' for lower, 's' for shirt, 't' for tshirt, 'z' to view inventory: ")

    if item_type == "l":
        quantity = int(input("Enter number of lowers to add: "))
        inventory_lower += quantity
        print("Total lowers =", inventory_lower)
    elif item_type == "s":
        quantity = int(input("Enter number of shirts to add: "))
        inventory_shirt += quantity
        print("Total shirts =", inventory_shirt)
    elif item_type == "t":
        quantity = int(input("Enter number of tshirts to add: "))
        inventory_tshirt += quantity
        print("Total tshirts =", inventory_tshirt)
    elif item_type == "z":
        print("Lowers =", inventory_lower)
        print("Shirts =", inventory_shirt)
        print("Tshirts =", inventory_tshirt)
    else:
        print("Invalid input")


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

    item_type = input("Add to cart: Press 'l' for lower, 's' for shirt, 't' for tshirt, 'b' to buy, 'o' for orders: ")

    if item_type == "l":
        quantity = int(input("Enter number of lowers to buy: "))
        if quantity > inventory_lower:
            print(f"{quantity} lowers are not available.")
        else:
            inventory_lower -= quantity
            print(f"{quantity} lowers added to your cart.")
            cart_lower += quantity
            if input("Enter 'c' to view cart or any key to continue: ") == "c":
                view_cart()

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
        view_cart()
        if input("Press 'a' to confirm purchase or any key to cancel: ") == "a":
            if cart_lower == 0 and cart_shirt == 0 and cart_tshirt == 0:
                print("Add items to your cart before buying.")
            else:
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

                order_lower, order_shirt, order_tshirt = cart_lower, cart_shirt, cart_tshirt
                cart_lower = cart_shirt = cart_tshirt = 0

    elif item_type == "o":
        print("Lowers in order =", order_lower)
        print("Shirts in order =", order_shirt)
        print("Tshirts in order =", order_tshirt)
    else:
        print("Invalid input")


initialize_orders()
initialize_inventory()
initialize_cart()
initiate()

while input("Press 0 to continue shopping or any key to exit: ") == "0":
    initiate()
else:
    print("Exited")
