# Section 1: Collecting fruit names
fruit_names = [] 
fruit_1 = input("Write fruit name: ")
fruit_names.append(fruit_1)
fruit_2 = input("Write fruit name: ")
fruit_names.append(fruit_2)
fruit_3 = input("Write fruit name: ")
fruit_names.append(fruit_3)
fruit_4 = input("Write fruit name: ")
fruit_names.append(fruit_4)
fruit_5 = input("Write fruit name: ")
fruit_names.append(fruit_5)
print(fruit_names)
print(type(fruit_names))

# Section 2: Collecting student marks
student_marks = []  
mark_1 = int(input("Write the marks of student 1: "))
student_marks.append(mark_1)
mark_2 = int(input("Write the marks of student 2: "))
student_marks.append(mark_2)
mark_3 = int(input("Write the marks of student 3: "))
student_marks.append(mark_3)
mark_4 = int(input("Write the marks of student 4: "))
student_marks.append(mark_4)
mark_5 = int(input("Write the marks of student 5: "))
student_marks.append(mark_5)
print(student_marks)
print(sorted(student_marks))  # Prints the sorted list of student marks
print(type(student_marks))

# Section 3: Summing a list of numbers
numbers = [1, 5, 7, 8] 
print(sum(numbers))
