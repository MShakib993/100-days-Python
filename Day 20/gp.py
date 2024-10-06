# A recursive function to calculate the sum of numbers from 0 to n
def sum(n):
    # Base case: when n is 0, return 0
    if (n == 0):
        return 0
    # Recursive call: return the sum of numbers up to n-1 plus n
    return sum(n-1) + n

# Call the sum function for n=5 and print the result
print(sum(5))


# Iterative version of sum calculation
def sum_iterative(n):
    total_sum = 0  # Initialize a variable to store the total sum
    # Loop from 1 to n (inclusive) and add each number to total_sum
    for i in range(1, n + 1):
        total_sum += i
    return total_sum  # Return the total sum after the loop completes

# Call the iterative function for n=5 and print the result
print(sum_iterative(5))


# This block takes user input and calculates the sum using a for loop
sum = 0  # Initialize sum to 0
num = int(input("Enter a num: "))  # Take user input and convert it to an integer
for i in range(0, num + 1):  # Loop from 0 to num (inclusive)
    print(i)  # Print the current value of i
    sum += i  # Add i to the sum
print(sum)  # Print the total sum


# Recursive function to calculate the sum of numbers from 0 to n
def sum_recursive(n):
    if n == 0:  # Base case: return 0 when n is 0
        return 0  
    return sum_recursive(n - 1) + n  # Recursive call

# Take user input and calculate the sum using recursion
num = int(input("Enter a number: "))  
result = sum_recursive(num)  # Call the recursive function
print(f"The sum of numbers from 0 to {num} is {result}")  # Print the result


# Recursive function to print a pattern of stars
def pattern(n):
    if n == 0:  # Base case: if n is 0, stop recursion
        return
    print("*" * n)  # Print n stars
    pattern(n-1)  # Recursive call with n-1 to print the next row

# Take user input and call the pattern function
pp = int(input("Enter a num: "))  
print(pattern(pp))  # Print the pattern (function returns None so no output)


# Function to convert inches to centimeters
def inch_cm(inch):
    return inch * 2.54  # Multiply inches by 2.54 to convert to centimeters

# Take user input and call the inch-to-cm conversion function
n = int(input("Enter a num: "))  
print(f"the value is {n} Inch to Cm {inch_cm(n)}")  # Print the result


# Function to remove a word from a list, removing the first instance of 'word'
def rem(list, word):
    for item in list:  # Iterate through each item in the list
        list.remove(word)  # Remove the word from the list
        return list  # Return the modified list (function stops after first removal)

# Define a list and remove the word 'Shakib' from it
l = ["Shakib", "Eksha", "Babul", "Mithi"]
print(rem(l, "Shakib"))  # Call the rem function and print the result


# Improved function to remove all instances of a word from a list
def rem1(list1, word):
    n = []  # Create an empty list to store the modified items
    for item in list1:  # Iterate through each item in the list
        if item != word:  # If the item is not the word
            n.append(item.strip(word))  # Remove occurrences of 'word' and add to n
    return n  # Return the modified list

# Define a list and remove occurrences of 'an' from the list
l1 = ["Harry", "Rohan", "Shubham", "an", "gg"]
print(rem1(l1, "an"))  # Call rem1 function and print the result


# Function to replace occurrences of a word in a list
def rem1(list1, word):
    n = []  # Create an empty list to store modified items
    for item in list1:  # Iterate through each item in the list
        if word in item:  # Check if the word is in the item
            print(item)  # Print the item if it contains the word
        n.append(item.replace(word, ""))  # Replace the word in the item and add to list
    return n  # Return the modified list

# Define a list and replace occurrences of 'an' in each item
l1 = ["Harry", "Rohan", "Shubham", "ffan", "gg"]
print(rem1(l1, "an"))  # Call rem1 function and print the result


# Function to replace a word in a list, only if it matches exactly
def rem1(list1, word):
    n = []  # Create an empty list to store modified items
    for item in list1:  # Iterate through each item in the list
        if item == word:  # If the item is exactly equal to the word
            print(item)  # Print the matching item
        else:
            n.append(item.replace(word, ""))  # Replace the word in the item
    return n  # Return the modified list

# Define a list and remove occurrences of 'an' where it matches exactly
l1 = ["Harry", "Rohan", "Shubham", "an", "gg"]
print(rem1(l1, "an"))  # Call rem1 function and print the result
