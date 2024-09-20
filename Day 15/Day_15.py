# Taking input from the user and converting it into an integer
a = int(input("Enter a number: "))  

# Initializing variables: i for the loop counter and sum for storing the total sum
i = 1  
sum = 0  

# Using a while loop to iterate through numbers from 1 to a-1
while(i < a):  
    sum += i  # Adding the value of i to sum
    i += 1  # Incrementing i by 1 for the next iteration
    print(i)  # Printing the value of i after it has been incremented

# After the loop ends, printing the total sum and the last value of i
print("The sum of numbers from 1 to", a-1, "is:", sum)  
print("The final value of i is:", i)







# Taking another input from the user for calculating the factorial
n = int(input("Enter a positive integer: "))  

# Initializing product to 1, as the factorial of a number starts with multiplication by 1
product = 1  

# Using a for loop to iterate through numbers from 1 to n (inclusive)
for i in range(1, n + 1):  
    product *= i  # Multiplying product by the current value of i
    print(i, end=" ")  # Printing each number from 1 to n in a single line

# Adding a new line after the loop completes
print()  

# Printing the final product, which is the factorial of n
print("The factorial of", n, "is:", product)  
