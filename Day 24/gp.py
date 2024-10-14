# Define a function that uses keyword-only arguments 'name' and 'age'
def nameage(*, name, age):
    # Print the name and age
    print(name, age)

# Call the function with keyword arguments
nameage(age=6, name="Shakib")  # Output: Shakib 6


# Define a function that takes a positional argument 'name', 
# and keyword-only arguments 'age' and 'city'
def namecityage(name, *, age, city):
    # Print a formatted string with name, age, and city
    print(f"My name is {name}, and my age is {age}, and I am from {city}")

# Call the function with a positional argument and keyword arguments
namecityage("Shakib", age=8, city="Katihar")  # Output: My name is Shakib and My age is 8 and I am from Katihar


# Define a function that returns the cube of a number
def cube(x):
    return x * x * x  # Calculate and return x^3

# Define a list of numbers
l = [1, 2, 3, 4, 5, 6]

# Use the map function to apply the 'cube' function to every element in the list 'l'
newl = list(map(cube, l))  # Convert the map object to a list of cubes
newl = list(map(cube, l))  # This line repeats the same operation

# Print the list of cubes
print(newl)  # Output: [1, 8, 27, 64, 125, 216]

# Do the same operation again, creating a new list 'newl1'
newl1 = list(map(cube, l))

# Print the second list of cubes
print(newl1)  # Output: [1, 8, 27, 64, 125, 216]


# Define a filter function that returns True if 'a' is greater than 4
def filter_fun(a):
    return a > 4  # Returns True if a > 4, else False

# Apply the filter function to 'newl1' and return only values greater than 4
newl2 = list(filter(filter_fun, newl1))  # Filtered list of cubes greater than 4

# Apply the filter function to 'l' (the original list) and filter values greater than 4
newl2 = list(filter(filter_fun, l))  # Filtered list from 'l', numbers greater than 4

# Print the filtered list
print(newl2)  # Output: [5, 6]


# Import 'reduce' function from 'functools' module
from functools import reduce

# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Define a function that adds two numbers
def mysum(x, y):
    return x + y  # Returns the sum of x and y

# Use 'reduce' to apply 'mysum' to all elements of the 'numbers' list, cumulatively adding them
sum = reduce(mysum, numbers)

# Print the sum of all numbers in the list
print(sum)  # Output: 36
