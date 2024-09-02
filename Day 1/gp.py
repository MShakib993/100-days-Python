var = "sHaKib"

# Using len() method to get the length of the string
print(len(var))  # Output: 6

# Using endswith() method to check if the string ends with "ib"
print(var.endswith("ib"))  # Output: True

# Using count() method to count the occurrences of "i" in the string
print(var.count("i"))  # Output: 1

# Using capitalize() method to capitalize the first letter of the string
b = var.capitalize()  
print(b)  # Output: "Shakib"

# Using upper() method to convert the string to uppercase
c = var.upper()  
print(c)  # Output: "SHAKIB"

# Using lower() method to convert the string to lowercase
d = var.lower()  
print(d)  # Output: "shakib"

# Using replace() method to replace "sHaKib" with "Babul"
e = var.replace("sHaKib", "Babul")  
print(e)  # Output: "Babul"

# Using find() method to find the index of the first occurrence of "b"
f = e.find("b")  
print(f)  # Output: 1

a = 123
# Using str() method to convert the integer to a string
b = str(a)  
print(type(b))  # Output: <class 'str'>  # The type of b is string

# Using escape sequences in strings
print("Sha\nkib")  # Output: "Sha" and "kib" on a new line
print("Sha\tkib")  # Output: "Sha" and "kib" separated by a tab space
print("Sha\\kib")  # Output: "Sha\kib"  # The backslash is escaped
print("Sha\'kib")  # Output: "Sha'kib"  # The single quote is escaped

hello = "Hello World"

# Using slicing to print the entire string
print(hello[0: ])  # Output: "Hello World"

# Using slicing to print the string except for the last character
print(hello[ :-1 ])  # Output: "Hello Worl"

# Using slicing to print the entire string
print(hello[ : ])  # Output: "Hello World"

# Using slicing with step to print every character except the last one
print(hello[ :-1:1])  # Output: "Hello Worl"

# Using slicing with step to print every second character except the last one
print(hello[ :-1:2])  # Output: "HloWl"

# Using split() method to split the string into a list of words
print(hello.split())  # Output: ["Hello", "World"]

s = "Hello eWorld"

# Using index() method to find the starting index of "World"
print(s.index("World"))  # Output: 7

# Using join() method to join a list of words into a single string with spaces
words = ["Hello", "World"]
print(" ".join(words))  # Output: "Hello World"
