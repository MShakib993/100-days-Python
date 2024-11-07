class Calculation:  # Corrected the class name to be capitalized
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b
        
    def add(self):
        return self.num1 + self.num2
        
    def sub(self):
        return self.num1 - self.num2

# Create an instance of Calculation
b = Calculation(10, 320)

# Print the results of addition and subtraction
print(b.add())  # This will print the result of addition
print(b.sub())  # This will print the result of subtraction
