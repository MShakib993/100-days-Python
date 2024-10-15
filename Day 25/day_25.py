list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

zipped = zip(list2, list1)
print(list(zipped))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]


sentence = "Hello, world! Welcome to Python."
words = sentence.split()  # Default separator (whitespace)
print(words)  # Output: ['Hello,', 'world!', 'Welcome', 'to', 'Python.']


data = "apple,banana,cherry"
fruits = data.split(",")
print(fruits)  # Output: ['apple', 'banana', 'cherry']


name = "Greekyshows"
str1 = name.replace("Greeky","Shakib")
print(str1)

sentence1 = "Hello world! Welcome to Python."
str2 = sentence1.split(" ")
print(str2)

list = ["my","Name","is","Shakib"]
str3 = "_".join(str2)
str4 = "".join(str2)
str5 = " ".join(list)
print(str5)
print(str3)
print(str4)



