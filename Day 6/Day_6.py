# Dictionary to store words and their translations
words = {
    "Kursi": "Chair",
    "Chabhi": "Key",
    "Kammal": "Blanket",
    "juta": "Shoes"
}

# Taking input from the user for a word and printing its translation from the dictionary
word = input("Write a word translation: ")
print(words[word])  # Accessing the dictionary to get the translation of the word

# Creating an empty set to store unique numbers
s = set()

# Taking multiple user inputs (integers) and adding them to the set
# Set is used because it automatically stores only unique numbers, removing duplicates
n = int(input("Write a number: "))
s.add(n)  # Adding the input number to the set
n = int(input("Write a number: "))
s.add(n)
n = int(input("Write a number: "))
s.add(n)
n = int(input("Write a number: "))
s.add(n)
n = int(input("Write a number: "))
s.add(n)
n = int(input("Write a number: "))
s.add(n)
n = int(input("Write a number: "))
s.add(n)
n = int(input("Write a number: "))
s.add(n)

# Printing the final set (only unique numbers will be printed)
print(s)

# Creating an empty dictionary to store names and languages
my_dict = {}

# Taking input for names and languages and updating the dictionary
# Dictionary stores each name (key) and its corresponding language (value)
name = input("write your name: ")
lang = input("write your language: ")
my_dict.update({name: lang})  # Adding name and language to the dictionary
name = input("write your name: ")
lang = input("write your language: ")
my_dict.update({name: lang})
name = input("write your name: ")
lang = input("write your language: ")
my_dict.update({name: lang})
name = input("write your name: ")
lang = input("write your language: ")
my_dict.update({name: lang})

# Printing the final dictionary with names and their languages
print(my_dict)
