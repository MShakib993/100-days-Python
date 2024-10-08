# Iterative function to compute the sum of the first 'n' numbers
def fun1(n):
    sum = 0
    # Loop from 1 to n, adding each number to sum
    for i in range(1, n + 1):
        sum += i
    return sum

# Call fun1 with n = 5 and print the result
print(fun1(5))  # Output will be 15

# Recursive function to compute the sum of the first 'n' numbers
def fun1(n):
    # Base case: if n is 1, return 1 (sum of the first number is 1)
    if n == 1:
        return 1
    # Recursive case: return n plus the sum of the numbers before it
    return n + fun1(n - 1)

# Call the recursive fun1 with n = 5 and print the result
print(fun1(5))  # Output will be 15

# Recursive function to compute the factorial of 'n'
def fun1(n):
    # Base case: if n is 1, return 1 (factorial of 1 is 1)
    if n == 1:
        return 1
    # Recursive case: return n multiplied by factorial of (n - 1)
    return n * fun1(n - 1)

# Call the recursive fun1 with n = 5 and print the result
print(fun1(5))  # Output will be 120 (since 5! = 5 * 4 * 3 * 2 * 1)

# Recursive function to compute the sum of digits of 'n'
def sum(n):
    # Base case: if n is 0, return 0 (no more digits to add)
    if n == 0:
        return 0
    # Recursive case: add the last digit of 'n' (n % 10) to the sum of the digits of the truncated number (n // 10)
    a = n % 10
    n = n // 10
    return a + sum(n)

# Call the sum function with n = 5568 and print the result
print(sum(5568))  # Output will be 24 (since 5 + 5 + 6 + 8 = 24)

# Recursive function to compute the sum of digits of 'n' (similar to the 'sum' function above)
def fun(n):
    # Base case: if n is 0, return 0
    if n == 0:
        return 0
    # Recursive case: add the last digit of 'n' (n % 10) to the sum of the digits of the truncated number (n // 10)
    return n % 10 + fun(n // 10)

# Call the fun function with n = 4567 and print the result
print(fun(4567))  # Output will be 22 (since 4 + 5 + 6 + 7 = 22)
