n = int(input("Enter a number: "))

# Question: Write code to check if the entered number is a prime number.
# The program should take a number as input and check if it's divisible by any number other than 1 and itself.

for i in range(2, n):
    if (n % i) == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")


n = int(input("Enter the number: "))

# Question: Write code to find the sum of the first N natural numbers.
# The program should calculate the sum of all numbers from 1 to the entered number.

i = 1
sum = 0
while(i <= n):
    sum += i
    i += 1

print(sum)
