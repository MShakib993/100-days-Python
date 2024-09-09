mark1 = int(input("Write mark of Student 1: "))
mark2 = int(input("Write mark of Student 2: "))
mark3 = int(input("Write mark of Student 3: "))
total_percentage = (100*(mark1+mark2+mark3))/300

if (total_percentage>=40 and mark1>=33 and mark3>=33 and mark2>=33):
    print("You are passed")
else:
    print("You are not passed")



p1 = "Hello"
p2 = "Busy"
p3 = "Cricket"
p4 = "Delhi"

message = input("Write a spam msg: ")

if(p1 in message) or (p2 in message) or (p3 in message) or (p4 in message):
    print("This is spam")
else:
    print("This is not spam")



username = input("Write a username: ")
if(len(username)<10):
    print("Your username has less then 10 Character")
else:
    print("Your username has more then 10 characters")


list1 = ["Shakib","Eksha","Babul","Mithi"]
name = input("Write a name: ")
if(name in list1):
    print("Name is present in list")
else:
    print("Name is not present in list")


a = 3457
b = str(a)
c = ''.join(reversed(b))  # Join the reversed iterator into a string
print(c)
print(type(b), b, len(b))



dict1 = {
    123:"One two three",
    2:"Two",
    3:"Three"
}
num = int(input("Write a num1: "))
print(dict1[num])

my_dict = {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "0":"zero",
    "8":"seven",
    "9":"eight",
}

string1 = input("Enter a number: ")
for val in string1:
    print(my_dict[val])


