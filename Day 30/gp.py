#Q1
num = int(input("Enter a num: "))  
# Accepts an integer input for the number of rows in the pyramid

for i in range(0, num):
    # Iterates through each row from 0 to num-1
    print(" " * (num - i - 1) + "*" * (2 * i + 1))
    # Prints spaces followed by stars to form the pyramid
    # " " * (num - i - 1) creates the leading spaces
    # "*" * (2 * i + 1) creates the number of stars per row


#Q2
num = int(input("Enter a num: "))
# Accepts an integer input to check for perfect square

sqr_root = num ** 0.5
# Calculates the square root of the input number

if sqr_root == int(sqr_root):
    # Checks if the square root is an integer (i.e., a perfect square)
    print(int(sqr_root), "is perfect square root of", num)
else:
    # Executes if the square root is not an integer
    print(num, "is not a perfect square root")


#Q3
nn = int(input("Enter a num1: "))
# Accepts an integer input as the starting number

for num in range(nn, 20):
    # Loops from the input number `nn` to 19
    if num > 1:
        # Skips numbers less than 2 (since prime numbers are greater than 1)
        for i in range(2, num):
            # Checks divisibility of the number from 2 to num-1
            if num % i == 0:
                break
        else:
            # If no divisors are found, it is a prime number
            print(num, "is a prime number")


#Q4
def cube(x):
    return x**3
# Defines a function to compute the cube of a number

n = int(input("Enter a number: "))
# Accepts an integer input

even_cubes = {}
# Initializes an empty dictionary to store cubes of even numbers

for i in range(2, n):
    # Loops through numbers from 2 to n-1
    if i % 2 == 0:
        # Checks if the number is even
        even_cubes[i] = cube(i)
        # Stores the cube of the even number in the dictionary

print(even_cubes)
# Prints the dictionary containing even numbers and their cubes


#Q5
dict = {}
# Initializes an empty dictionary

n = int(input("Enter the number of times : "))
# Accepts an integer input for the number of iterations

for i in range(0, n + 1):
    # Loops through numbers from 0 to n
    if i % 2 == 0:
        # Checks if the number is even
        key = i
        # Sets the number as the dictionary key
        value = i ** 3
        # Sets the cube of the number as the dictionary value
        dict[key] = value
        # Adds the key-value pair to the dictionary

print(dict)
# Prints the final dictionary containing even numbers and their cubes



#Q6
def count_consonant(a):
    vowels = set('aeiou')
    # Defines a set of vowels for quick lookups

    count = 0
    # Initializes a counter for consonants

    for char in a.lower():
        # Iterates over each character in the input string (converted to lowercase)
        if char.isalpha() and char not in vowels:
            # Checks if the character is an alphabet and not a vowel
            count += 1
            # Increments the consonant count if the condition is met

    return count
    # Returns the final count of consonants

a = input("Enter the string: ")
# Accepts a string input

result = count_consonant(a)
# Calls the function to count consonants in the string

print("Number of consonants:", result)
# Prints the number of consonants found


