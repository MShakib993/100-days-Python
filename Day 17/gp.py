def ask_password():
    # Asks the user to input a password
    password = input("Enter a password: ")
    # Calls the function to check if the password is valid
    check_password(password)

def check_password(check_pass):
    # Checks if the password meets the required conditions
    if len(check_pass) < 8:
        # Prints an error if the password is shorter than 8 characters
        print("Invalid Password: Must be at least 8 characters long")
        return
    
    # Initializing flags to check for various password requirements
    flag_upper = 0  # To track if there is an uppercase letter
    flag_lower = 0  # To track if there is a lowercase letter
    flag_num = 0    # To track if there is a number
    flag_symbol = 0 # To track if there is a symbol
    
    # Looping through each character in the password
    for char in check_pass:
        if char.isupper():
            # Increment the uppercase flag if an uppercase letter is found
            flag_upper += 1
        elif char.islower():
            # Increment the lowercase flag if a lowercase letter is found
            flag_lower += 1
        elif char.isdigit():
            # Increment the number flag if a digit is found
            flag_num += 1
        else:
            # Increment the symbol flag if any other character is found (symbol)
            flag_symbol += 1
    
    # Calls the validation function, passing in the flags
    validate(flag_lower, flag_num, flag_symbol, flag_upper)

def validate(a, b, c, d):
    # Function to validate the password based on flags and give feedback
    missing = []  # List to store missing elements
    
    # Checking which requirements are missing and adding to the list
    if a == 0:
        missing.append("lowercase letter")
    if b == 0:
        missing.append("number")
    if c == 0:
        missing.append("symbol")
    if d == 0:
        missing.append("uppercase letter")
    
    # If no elements are missing, the password is valid
    if len(missing) == 0:
        print("Valid Password")
    else:
        # If some elements are missing, list them
        print("Invalid Password: Missing", ", ".join(missing))

# Initiates the password prompt and validation process
ask_password()
