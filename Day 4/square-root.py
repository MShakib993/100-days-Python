# Example number
num = int(input("Write a number: "))

# Calculate the square root using exponentiation (raising to the power of 0.5)
square_root = num ** 0.5

# Check if it's a perfect square
if square_root == int(square_root):
    print(num, "is a perfect square, and its square root is", int(square_root))
else:
    print(num, "is not a perfect square.")
