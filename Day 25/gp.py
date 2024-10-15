
list1 = [1, 2, 3]  # Creates a list containing integers 1, 2, 3
list2 = ['a', 'b', 'c']  # Creates another list containing characters 'a', 'b', 'c'

zipped = zip(list2, list1)  # Combines the two lists element by element into pairs using zip
print(list(zipped))  # Converts the zipped object into a list and prints it. Output will be [('a', 1), ('b', 2), ('c', 3)]

# ---------------------------------------

sentence = "Hello, world! Welcome to Python."  # Creates a string with a sentence
words = sentence.split()  # Splits the sentence into words based on whitespace (default split behavior)
print(words)  # Prints the list of words. Output will be ['Hello,', 'world!', 'Welcome', 'to', 'Python.']

# ---------------------------------------

data = "apple,banana,cherry"  # Creates a string containing fruit names separated by commas
fruits = data.split(",")  # Splits the string into a list using a comma as the delimiter
print(fruits)  # Prints the list of fruits. Output will be ['apple', 'banana', 'cherry']

# ---------------------------------------

name = "Greekyshows"  # Creates a string 'Greekyshows'
str1 = name.replace("Greeky","Shakib")  # Replaces 'Greeky' in the string with 'Shakib'
print(str1)  # Prints the updated string. Output will be 'Shakibshows'

# ---------------------------------------

sentence1 = "Hello world! Welcome to Python."  # Creates another string with a sentence
str2 = sentence1.split(" ")  # Splits the sentence into words using a space (" ") as the delimiter
print(str2)  # Prints the list of words. Output will be ['Hello', 'world!', 'Welcome', 'to', 'Python.']

# ---------------------------------------

list = ["my", "Name", "is", "Shakib"]  # Creates a list of strings
str3 = "_".join(str2)  # Joins the words in the list 'str2' with underscores ('_') between them
str4 = "".join(str2)  # Joins the words in the list 'str2' with no space (empty string) between them
str5 = " ".join(list)  # Joins the elements in the 'list' with spaces (' ') between them
print(str5)  # Prints 'my Name is Shakib'
print(str3)  # Prints the string with underscores between words, e.g., 'Hello_world!_Welcome_to_Python.'
print(str4)  # Prints the string with no spaces, e.g., 'Helloworld!WelcometoPython.'
