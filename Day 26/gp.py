f = open("file.txt" , "r")  # Opens the file 'file.txt' in read mode ("r"). If the file doesn't exist, it will raise an error.
data = f.read()  # Reads the entire content of 'file.txt' and stores it in the variable 'data'.
print(data)  # Prints the content of 'data' (the content of 'file.txt') to the console.
f.close()  # Closes the file 'file.txt' to release the file handle and system resources.



st = "Hey Shakib How are you"  # Creates a string 'st' with the value "Hey Shakib How are you".
ff = open("myfile.txt" , "w")  # Opens (or creates) the file 'myfile.txt' in write mode ("w"). If the file exists, it will be overwritten.
ff.write(st)  # Writes the string 'st' ("Hey Shakib How are you") to 'myfile.txt'.
ff.close()  # Closes the file 'myfile.txt' after writing, ensuring all data is saved properly.





st1 = "Hey Shakib How are you"  # Creates another string 'st1' with the same value as before ("Hey Shakib How are you").
ff1 = open("myfile.txt" , "a")  # Opens the file 'myfile.txt' in append mode ("a"), allowing data to be added to the end without erasing the previous content.
ff1.write(st1)  # Appends the string 'st1' to 'myfile.txt'. The file now contains "Hey Shakib How are youHey Shakib How are you".
ff1.close()  # Closes the file 'myfile.txt' after appending.


fff = open("file.txt")  # Opens 'file.txt' in read mode (default is read mode if not explicitly specified).
liner = fff.readlines()  # Reads all the lines of 'file.txt' into a list of strings called 'liner', where each line is an element in the list.
print(liner, type(liner))  # Prints the list 'liner' and the type of the variable (which will be a 'list').
fff.close()  # Closes the file 'file.txt' after reading.
