# String Formatting examples
frmt1 = "Welcome to {name} in {college}".format(name="Coding Block", college="LPU")
print(frmt1)  # Output: Welcome to Coding Block in LPU
# Question: How does named placeholder formatting work in Python?

frmt2 = "Welcome to {0} in {1}".format("Coding block", "LPU")
print(frmt2)  # Output: Welcome to Coding block in LPU
# Question: How do positional arguments work with the .format() method?

frmt3 = "Welcome to {} in {}".format("Coding Block", "LPU")
print(frmt3)  # Output: Welcome to Coding Block in LPU
# Question: How do empty placeholders work in the .format() method?

frmt4 = "Welcome to {a:^10} in {b:>10}".format(a="sk", b="LPU")
print(frmt4)  # Output: Welcome to    sk     in        LPU
# Question: How does formatting width and alignment work using .format()?

# Pyramid pattern using loops
n = 5
for i in range(1, n+1):  # Loop through rows (i from 1 to 5)
    for j in range(i, n):  # Loop for spaces before stars, decreases as i increases
        print(" ", end="")
    for k in range(2*i-1):  # Loop to print stars in increasing numbers (odd count)
        print("*", end="")
    print()  # Move to the next line
# Question: How does nested looping help in creating a pyramid pattern of stars?

# Another way to print a pyramid using simpler code
n = 5
for i in range(n):  # Loop through rows (i from 0 to 4)
    print(" " * (n - i - 1) + "*" * (2 * i + 1))  # Combine spaces and stars in one print statement
# Question: How can a pyramid pattern be printed with minimal use of loops?

# 'X' pattern with stars and underscores
n = 5
for i in range(n):
    if i == 0 or i == n-1:  # First and last rows are printed with "x_" repeated n times
        print("{}".format("x_"*n))
    else:
        print("*{}*_".format("_"*(2*n-3)))  # Middle rows are printed with stars at ends and underscores in between
# Question: How does this code print an 'X' pattern using conditional logic inside loops?

# Prime number detection between a range
a = int(input("Enter a number: "))  # Take user input for starting number
for num in range(a, 20):  # Check numbers in the range [a, 20)
    if num > 1:  # Only check numbers greater than 1 (since 0 and 1 are not prime)
        for i in range(2, num):  # Check if num is divisible by any number from 2 to num-1
            if num % i == 0:  # If divisible, it's not prime, so break
                break
        else:
            print(num, "is a prime number")  # If no divisors are found, num is prime
# Question: How does the nested loop check if a number is prime within a given range?
