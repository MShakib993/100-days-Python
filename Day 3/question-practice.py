# Q1 insert a fruit in list in position 1
a = ["Appple","Orange","Grapes","Banana"]
a.insert(1 , "Mango")
print(a)

# Q2 What is difference between pop and remove

b = ["Shakib",56,"Eksha","22","Babul","Mithi"]
b.pop(5)
print(b)
b.remove("Shakib")
print(b)

#imp--- Difference btwn pop and remove is in pop we target anything by indexing and in remove we target anything by item names.


# Q3 sort and sort decending

numbers = [5,90,1,0,4,9]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

# Q4 Merge List
List1 = [ 1,5,5,4,3,7]
List2 = [ 1,5,5,4,3,7]
print(List1+List2)
print(List1[1])
print(List1[1:])

# Q5 List Comphrension
Square = [x**2 for x in range(1,20)]
print(Square)


# Q6 filter out numbers
number = [1,2,3,4,5,6,7,8,9,10]
odd_number = [x for x in number if x%2!=0] 
print(odd_number)
even_number = [x for x in number if x%2==0] 
print(even_number)

# Q7 Filter out number in list conphrension

number1 = [x**2 for x in range(1,20)]
odd = [x for x in number1 if x%2!=0]
print(odd)
even = [x for x in number1 if x%2==0]
print(even)


# Q8 Clone list 
original = [1,5,7]
clone = original.copy()
clone.append(6)
print(original)
print(clone)

# Q9 Remove duplicates while preserving order
number2 = [1,2,2,3,5,66,6,6,8]
unique_num = []
for num in number2:
    if num not in unique_num:
        unique_num.append(num)
print(unique_num)
