def check_password():
    password = "5678"
    passs = input("Enter your password: ")
    if passs == password:
        print('''
              Press 1 for Balance
              Press 2 for Credit
              Press 3 for Debit
              Press 4 for Change Password
              Press 0 for Exit
       ''')
        choice = int(input("Enter your choice: "))
        if choice == 1:
            check_balance()
        elif choice == 2:
            credit()
        elif choice == 3:
            debit()
        elif choice == 4:
            change_password()
        else:
            print("Thank you!")
    else:
        print("The password is wrong")

balance = 100000  

def check_balance():
    print("Your current balance is:", balance)

def credit():
    global balance 
    amount = int(input("Enter the amount you want to credit: "))
    balance = balance + amount
    check_balance()

def debit():
    global balance  
    amount = int(input("Enter the amount you want to debit: "))
    if amount > balance:
        print("Insufficient balance")
    else:
        balance -= amount  
        check_balance()

def change_password():
    global password
    new_password = input("Enter your new password: ")
    password = new_password
    print("Password changed successfully!")


check_password()
