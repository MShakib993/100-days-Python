num = int(input("write a number: "))
num1 = num  # Store the original number
deg = 0

# Calculate the number of digits in the number
while num != 0:
    q = num // 10
    deg += 1
    num = q

# Reset num to original value
num = num1
temp = 0

# Calculate the sum of digits raised to the power of the number of digits
while num != 0:
    q = num // 10
    r = num % 10
    temp += (r) ** deg
    num = q

# Check if the sum is equal to the original number
if temp == num1:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
