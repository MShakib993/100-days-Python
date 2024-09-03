# num1 = int(input("Enter num1: "))
# operation = input("operation: ")
# num2 = int(input("num2  "))
# if operation == "+":
#     sum= num1 + num2
#     print("Sum is",sum)
# elif operation == "-":
#     sub = num1 - num2
#     print("sub is", sub)
# elif operation == "*":
#     num= num1*num2
#     print("multiple", num)




# **Question:**

# Write a Python program that acts as a simple calculator. The program should prompt the user to input two numbers (`num1` and `num2`) and an arithmetic operation (`+`, `-`, or `*`). Based on the operation entered by the user, the program should perform the corresponding calculation (addition, subtraction, or multiplication) and print the result.

# Prompt the user to enter the first number
num1 = int(input("Enter num1: "))

# Prompt the user to enter the desired arithmetic operation (+, -, or *)
operation = input("operation: ")

# Prompt the user to enter the second number
num2 = int(input("num2  "))

# Check if the operation is addition
if operation == "+":
    # Calculate the sum of num1 and num2
    sum = num1 + num2
    # Print the result of the addition
    print("Sum is", sum)

# Check if the operation is subtraction
elif operation == "-":
    # Calculate the difference between num1 and num2
    sub = num1 - num2
    # Print the result of the subtraction
    print("sub is", sub)

# Check if the operation is multiplication
elif operation == "*":
    # Calculate the product of num1 and num2
    num = num1 * num2
    # Print the result of the multiplication
    print("multiple", num)
