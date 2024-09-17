# Function to print first and last names
def names(a, b):
    # The function receives two parameters, 'a' and 'b', and prints them as first and last names.
    print("First name is: ", a)
    print("Last name is: ", b)

# Function to ask user for their first and last names and pass them to the 'names' function
def ask():
    # Ask the user for their first name
    first_name = input("Enter your first name: ")
    
    # Ask the user for their last name
    last_name = input("Enter your last name: ")
    
    # Pass the user input (first and last name) to the 'names' function
    names(first_name, last_name)

# Call the 'ask' function to start the program
ask()

# Q: What happens if you input numbers or special characters as the first or last name?
# Q: Can you modify the code to handle empty inputs for the first or last name?

# Program to print multiplication table of a number
n = int(input("Enter a num: "))  # Ask the user to input a number
i = 1  # Initialize the loop counter

# While loop to print the multiplication table up to 10
while(i < 11):
    print(f"{n} X {i} = {n*i}")  # Print the result of n multiplied by i
    i += 1  # Increment the counter

# Q: What would happen if you set 'i = 11' initially? Would the loop execute?

# Using a 'for' loop to print the multiplication table of the same number
for i in range(1, 11):
    print(f"{n} X {i} = {n*i}")  # Print the result of n multiplied by i

# Q: How is the 'for' loop different from the 'while' loop in terms of initialization and termination?

# Program to check if a number is prime
num = int(input("Enter a num: "))  # Ask the user to input another number

# For loop to check if the number is divisible by any number between 2 and 'num'
for i in range(2, num):
    if (num % i) == 0:
        print("It is not a prime number")  # If divisible by any 'i', it's not prime
        break  # Exit the loop if a divisor is found
    else:
        print("It is a prime number")  # If no divisors are found, it's prime

# Q: What happens when 'num' is less than or equal to 1? Can you improve this code to handle such cases?
# Q: Why do we start the loop at 2? Could you start at 1, and what would the result be?
