# Set the number of rows for the pyramid pattern
n = 5

# Loop through each row from 0 to n-1
for i in range(n):
    # Print spaces: (n - i - 1) spaces followed by stars: (2 * i + 1) stars
    print(" " * (n - i - 1) + "*" * (2 * i + 1))

# Set the number of rows for the x pattern
n = 5

# Loop through each row from 0 to n-1
for i in range(n):
    # If it's the first row (i == 0) or the last row (i == n-1)
    if i == 0 or i == n-1:
        # Print the character 'x_' repeated n times
        print("{}".format("x_" * n))
    else:
        # Print '*' followed by (2*n - 3) underscores and then another '*'
        print("*{}*_".format("_" * (2 * n - 3)))

# Prompt the user to enter a number and convert it to an integer
a = int(input("Enter a number: "))

# Loop through numbers from the entered number (a) to 19
for num in range(a, 20):
    # Check if the number is greater than 1 (to exclude 0 and 1, which are not prime)
    if num > 1:
        # Loop through potential divisors from 2 to num - 1
        for i in range(2, num):
            # If num is divisible by any i, it is not a prime number
            if num % i == 0:
                break
        else:
            # If the loop completed without breaking, num is prime
            print(num, "is a prime number")

# Set the number of rows for the pyramid pattern
n = 5

# Loop through each row from 1 to n (inclusive)
for i in range(1, n + 1):
    # Print spaces for alignment: n - i spaces
    for j in range(i, n):
        print(" ", end="")
    
    # Print stars: (2*i - 1) stars for the current row
    for k in range(2 * i - 1):
        print("*", end="")
    
    # Move to the next line after printing the stars for the current row
    print()
