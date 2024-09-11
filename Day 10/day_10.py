# Prompt the user to input a number and convert it to an integer
num = int(input("Write a number: "))

# Initialize a variable to store the sum of the digits of the number
sum = 0

# Use a while loop to continue as long as the number is not 0
while(num != 0):
    # Perform integer division to get the quotient (i.e., the number without the last digit)
    q = num // 10
    
    # Calculate the remainder (i.e., the last digit of the number)
    r = num % 10
    
    # Add the last digit (remainder) to the sum
    sum += r
    
    # Update the number by removing the last digit (use the quotient)
    num = q

# After the loop finishes, print the sum of the digits
print(sum)
