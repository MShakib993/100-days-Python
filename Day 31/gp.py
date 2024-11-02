# Section 1: Zipping Lists
list1 = ["a", "b", "c", "d"]  # List of strings
list2 = [1, 2, 3, 4]          # List of integers
zipped_list = list(zip(list1, list2))  # Zips list1 and list2 into pairs and converts to a list
print(zipped_list)             # Output: [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

# Section 2: Zipping Tuples
tup1 = (1, 2, 3)               # Tuple of integers
tup2 = ('a', 'b', 'c')         # Tuple of strings
zipped_tuple = tuple(zip(tup1, tup2))  # Zips tup1 and tup2 into pairs and converts to a tuple
print(zipped_tuple)            # Output: ((1, 'a'), (2, 'b'), (3, 'c'))

# Section 3: Zipping Strings
string1 = 'abc'                # String with 3 characters
string2 = '123'                # String with 3 characters (numbers as characters)
zipped_string = list(zip(string1, string2))  # Zips characters of string1 and string2 into pairs and converts to a list
print(zipped_string)           # Output: [('a', '1'), ('b', '2'), ('c', '3')]

# Section 4: Zipping Sets
set1 = {1, 2, 3}               # Set of integers
set2 = {'x', 'y', 'z'}         # Set of strings
zipped_set = list(zip(set1, set2))  # Zips elements from set1 and set2 into pairs and converts to a list
print(zipped_set)              # Output: [(1, 'x'), (2, 'y'), (3, 'z')] or similar (order may vary)

# Section 5: Zipping Dictionaries by Keys
dict1 = {'key1': 1, 'key2': 2}  # Dictionary with keys 'key1' and 'key2'
dict2 = {'keyA': 10, 'keyB': 20}  # Dictionary with keys 'keyA' and 'keyB'
zipped_dict_keys = list(zip(dict1, dict2))  # Zips keys from dict1 and dict2, creating pairs of keys only
print(zipped_dict_keys)         # Output: [('key1', 'keyA'), ('key2', 'keyB')]

# Section 6: Writing to a File Using 'with'
intro_text = "Hello, I am Shakib"     # String to write to the file
with open("myfile.txt", "w") as file_writer:  # Opens 'myfile.txt' in write mode and assigns to file_writer
    print(file_writer.write(intro_text))  # Writes intro_text to the file and prints number of characters written

# Section 7: Writing to a File Using Open and Close
statement = "Hi, How are you"          # String to write to the file
file_writer2 = open("myfile.txt", "w")  # Opens 'myfile.txt' in write mode (overwrites if exists)
data_written = file_writer2.write(statement)  # Writes statement to the file and saves number of characters written to data_written
file_writer2.close()                    # Closes the file to save changes

# Section 8: Reading All Lines from a File
file_reader = open("rd.txt")           # Opens 'rd.txt' in read mode
all_lines = file_reader.readlines()     # Reads all lines from the file and stores in all_lines as a list of strings
print(all_lines)                        # Prints list of lines from the file
file_reader.close()                     # Closes the file after reading

# Section 9: Reading Lines One by One
file_reader2 = open("rd.txt")           # Opens 'rd.txt' in read mode
line1 = file_reader2.readline()         # Reads the first line from the file
print(line1)                            # Prints the first line

line2 = file_reader2.readline()         # Reads the second line from the file
print(line2)                            # Prints the second line

line3 = file_reader2.readline()         # Reads the third line from the file
print(line3)                            # Prints the third line

file_reader2.close()                    # Closes the file after reading

# Section 10: Reading Lines in a Loop Until End of File
file_reader3 = open("rd.txt")           # Opens 'rd.txt' in read mode
line = file_reader3.readline()          # Reads the first line
while line != "":                       # Loops until there are no more lines
    print(line)                         # Prints the current line
    line = file_reader3.readline()      # Reads the next line
file_reader3.close()                    # Closes the file after reading all lines

# Section 11: Appending to a File
additional_text = "Hello again!"        # String to append to the file
with open("myfile.txt", "a") as file_appender:  # Opens 'myfile.txt' in append mode and assigns to file_appender
    file_appender.write(additional_text)        # Appends additional_text to the file
