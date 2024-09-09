# QUESTION-1

mark1 = int(input("Write mark of Student 1: "))  # Get mark of Student 1
mark2 = int(input("Write mark of Student 2: "))  # Get mark of Student 2
mark3 = int(input("Write mark of Student 3: "))  # Get mark of Student 3

# Calculate the total percentage for all three students
total_percentage = (100 * (mark1 + mark2 + mark3)) / 300  

# Check if the percentage is above 40 and all marks are above 33
if total_percentage >= 40 and mark1 >= 33 and mark2 >= 33 and mark3 >= 33:  
    print("You are passed")  # Print pass message
else:
    print("You are not passed")  # Print fail message



# QUESTION-2

# Predefined spam words
p1 = "Hello"
p2 = "Busy"
p3 = "Cricket"
p4 = "Delhi"

message = input("Write a spam msg: ")  # Input message from the user

# Check if any spam word is present in the message
if p1 in message or p2 in message or p3 in message or p4 in message:  
    print("This is spam")  # Print if the message is spam
else:
    print("This is not spam")  # Print if the message is not spam


# QUESTION-3

username = input("Write a username: ")  # Get username from the user

# Check the length of the username
if len(username) < 10:  
    print("Your username has less than 10 characters")  # Print if username is short
else:
    print("Your username has more than 10 characters")  # Print if username is long




# QUESTION-4

list1 = ["Shakib", "Eksha", "Babul", "Mithi"]  # Predefined list of names

name = input("Write a name: ")  # Get name from the user

# Check if the name is present in the list
if name in list1:  
    print("Name is present in the list")  # Print if the name is found
else:
    print("Name is not present in the list")  # Print if the name is not found


# QUESTION-5

a = 3457  # Given number

b = str(a)  # Convert the number to a string
c = ''.join(reversed(b))  # Reverse the string and join it back into a string

print(c)  # Print the reversed number
print(type(b), b, len(b))  # Print the type, original string, and its length


# QUESTION-6

dict1 = {  # Predefined dictionary with numbers and their words
    123: "One two three",
    2: "Two",
    3: "Three"
}

num = int(input("Write a num1: "))  # Get a number from the user

print(dict1[num])  # Print the corresponding word from the dictionary


# QUESTION-7

my_dict = {  # Dictionary mapping digits to words
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "0": "zero",
    "8": "seven",  # This seems to be a typo; 8 should map to "eight"
    "9": "eight",  # 9 should map to "nine"
}

string1 = input("Enter a number: ")  # Get a number as a string

# Loop through each character in the string and print its corresponding word
for val in string1:  
    print(my_dict[val])  # Print the word corresponding to each digit
