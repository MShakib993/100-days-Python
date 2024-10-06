def sum(n):
    if (n == 0):
        return 0
    return sum(n-1) + n
print(sum(5))


def sum_iterative(n):
    total_sum = 0 
    for i in range(1, n + 1):
        total_sum += i
    return total_sum
print(sum_iterative(5))


sum = 0
num = int(input("Enter a num: "))
for i in range(0,num+1):
    print(i)
    sum += i
print(sum)


def sum_recursive(n):
    if n == 0:
        return 0  
    return sum_recursive(n - 1) + n

num = int(input("Enter a number: "))
result = sum_recursive(num)
print(f"The sum of numbers from 0 to {num} is {result}")

def pattern(n):
    if n == 0:
        return
    print("*" * n)
    pattern(n-1)
pp = int(input("Enter a num: "))
print(pattern(pp))


def inch_cm(inch):
    return inch * 2.54
n = int(input("Enter a num: "))
print(f"the value is {n} Inch to Cm {inch_cm(n)}")


def rem(list , word):
    for item in list:
        list.remove(word)
        return list
l = ["Shakib","Eksha","Babul","Mithi"]
print(rem(l,"Shakib"))



def rem1(list1,word):
    n = []
    for item in list1:
        if(item != word):
            n.append(item.strip(word))
    return n
l1 = ["Harry", "Rohan" , "Shubham" , "an" , "gg"]
print(rem1(l1,"an"))



def rem1(list1, word):
    n = []
    for item in list1:
        if word in item:
            print(item) 
        n.append(item.replace(word, ""))
    return n

l1 = ["Harry", "Rohan", "Shubham", "ffan", "gg"]
print(rem1(l1, "an"))


def rem1(list1, word):
    n = []
    for item in list1:
        if item == word:
            print(item)
        else:
            n.append(item.replace(word, ""))
    return n

l1 = ["Harry", "Rohan", "Shubham", "an", "gg"]
print(rem1(l1, "an"))
