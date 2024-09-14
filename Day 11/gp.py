# Prompt the user to input a message
user_message = input("Write something: ")

# Check if the word "harry" (case insensitive) is in the user's message
if "harry" in user_message.lower():
    print("This is talking about Harry")
else:
    print("This is not talking about Harry")


# Define a list of names
name1 = "Shakib"
name2 = "Zamin"
name3 = "Mithi"
name4 = "Eksha"

# Prompt the user to input a message
user_message = input("Write something: ")

# Check if any of the defined names are present in the user's message
if name1 in user_message or name2 in user_message or name3 in user_message or name4 in user_message:
    print("This is spam")
else:
    print("Clear")


# Initialize a variable to 5
initial_value = 5

# Loop through numbers from 0 to 9
for current_value in range(10):
    print(current_value)


# Initialize a counter variable
counter = 0

# Loop until the counter variable is less than 5
while counter < 5:
    print("Shakib")
    counter += 1


# Define a list of names
names_list = ["Shakib", "Mithi", "Babul", "Eksha", "Zamin"]

# Loop through each name in the list and print it
for name in names_list:
    print(name)
else:
    print("End")


# Initialize a counter variable
counter = 0

# Loop through the list using index-based access
while counter < len(names_list):
    print(names_list[counter])
    counter += 1


# Prompt the user to input a number
table_number = int(input("Write a number: "))

# Print the multiplication table for the entered number
for multiplier in range(1, 11):
    print(f"{table_number} X {multiplier} = {table_number * multiplier}")


# Define a list of names
names_list = ["Shakib", "Shubham", "Sneha", "Shreya"]

# Loop through each name in the list
for name in names_list:
    # Check if the name starts with the letter 'S'
    if name.startswith("S"):
        print(name)
