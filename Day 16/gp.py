# Pattern 1: Pyramid Pattern
# Question:
# Write a Python program that takes an input number num1 and prints a pyramid pattern of stars (*). The pyramid should have a height of num1-1, and each row should be centered with increasing stars.
num1 = int(input("Enter a num: "))
for i in range(1,num1):
    print(" " * (num1-i), end="")
    print("*" * (2*i-1), end="")
    print()


# Pattern 2: Right-Angled Triangle
# Question:
# Write a Python program that takes an input number num1 and prints a right-angled triangle of stars. The triangle should have num1-1 rows, with the number of stars in each row increasing from 1 to num1-1.
num1 = int(input("Enter a num: "))
for i in range(1,num1):
    print("*" * i)


# Pattern 3: Hollow Square
# Question:
# Write a Python program that takes an input number num2 and prints a hollow square pattern of stars. The square should have num2 rows and columns, with the border filled with stars and the inside being hollow.
num2 = int(input("Enter a num1: "))
for i in range(1, num2+1):
    if(i==1 or i == num2):
        print("*" * num2, end="")
    else:
        print("*", end="")
        print(" " * (num2-2), end="")
        print("*", end="")
    print("")


# Pattern 4: Hollow Rectangle
# Question:
# Write a Python program that takes an input number n and prints a hollow rectangle of stars. The rectangle should have n rows, with the first and last rows completely filled with stars, and the middle rows containing stars at the beginning and end, leaving the center empty.
n = int(input("Enter the number: "))
for i in range(1, n+1): 
    if(i==1 or i==n):
        print("*" * n, end="")
    else:
        print("*", end="")
        print(" " * (n-2), end="")
        print("*", end="")
    print("")





