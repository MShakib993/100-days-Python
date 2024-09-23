def ask_password():
    password = input("Enter a password: ")
    check_password(password)

def check_password(check_pass):
    if len(check_pass) < 8:
        print("Invalid Password: Must be at least 8 characters long")
        return
    
    flag_upper = 0
    flag_lower = 0
    flag_num = 0
    flag_symbol = 0
    
    for char in check_pass:
        if char.isupper():
            flag_upper += 1
        elif char.islower():
            flag_lower += 1
        elif char.isdigit():
            flag_num += 1
        else:
            flag_symbol += 1
    
    validate(flag_lower, flag_num, flag_symbol, flag_upper)

def validate(a, b, c, d):
    missing = []
    if a == 0:
        missing.append("lowercase letter")
    if b == 0:
        missing.append("number")
    if c == 0:
        missing.append("symbol")
    if d == 0:
        missing.append("uppercase letter")
    
    if len(missing) == 0:
        print("Valid Password")
    else:
        print("Invalid Password: Missing", ", ".join(missing))

ask_password()
