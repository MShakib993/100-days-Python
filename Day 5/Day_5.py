# **Question:**

# Write a Python program that prompts the user to input a number and then prints a right-angled triangle pattern of asterisks (`*`). The number of rows in the triangle should be equal to the input number. For example, if the user inputs `5`, the program should output:

# ```
# *
# **
# ***
# ****
# *****
# ```

num = int(input("Write a num: "))
for i in range(1, num +1):
    print("*" * i)