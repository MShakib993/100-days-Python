# Take an integer input from the user and store it in the variable 'n'
n = int(input("Enter a number: "))

# Define a function 'factorial' to calculate the factorial of a number using recursion
def factorial(g):
    # Base case: If the number is 1 or 0, return 1 (since 0! = 1 and 1! = 1)
    if g == 1 or g == 0:
        return 1
    # Recursive case: Multiply the number 'g' by the factorial of (g-1)
    return g * factorial(g - 1)

# Print the factorial of 'n' by calling the 'factorial' function
print(f"The factorial of {n} is {factorial(n)}")

# Define a function 'greatest' to find the greatest of three numbers 'a', 'b', and 'c'
def greatest(a, b, c):
    # If 'a' is greater than both 'b' and 'c', print 'a'
    if a > b and a > c:
        print(a)
    # If 'b' is greater than both 'a' and 'c', print 'b'
    elif b > a and b > c:
        print(b)
    # Otherwise, 'c' is the greatest, so print 'c'
    else:
        print(c)

# Take three integer inputs from the user and store them in 'd', 'e', and 'f'
d = int(input("Enter the first number: "))
e = int(input("Enter the second number: "))
f = int(input("Enter the third number: "))

# Call the 'greatest' function to print the greatest of 'd', 'e', and 'f'
greatest(d, e, f)

# Take an integer input representing Fahrenheit temperature and store it in 'fern'
fern = int(input("Enter a temperature in Fahrenheit: "))

# Define a function 'fern_to_cel' to convert Fahrenheit to Celsius
def fern_to_cel(f):
    # Convert Fahrenheit to Celsius using the formula and return the result
    return 5 * (f - 32) / 9

# Convert 'fern' to Celsius and store the result in 'c'
c = fern_to_cel(fern)

# Print the converted temperature rounded to 2 decimal places
print(f"The temperature is {round(c, 2)}°C")
