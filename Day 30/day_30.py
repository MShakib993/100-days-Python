num = int(input("Enter a num: "))
for i in range(0,num):
    print(" "*(num-i-1)+"*"*(2*i+1))




num = int(input("Enter a num: "))
sqr_root = num ** 0.5
if sqr_root == int(sqr_root):
    print(int(sqr_root),"is perfect sqr root of",num)
else:
    print(num ,"is not a perfect sqaure root")



nn = int(input("Enter a num1: "))
for num in range(nn , 20):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num ,"is a prime number")


def cube(x):
    return x**3  

n = int(input("Enter a number: "))

even_cubes = {}

for i in range(2, n):
    if i % 2 == 0:
        even_cubes[i] = cube(i)

print(even_cubes)


dict = {}
n = int(input("Enter the number of times : "))
for i in range(0,n+1):
    if(i%2 == 0):
        key = i
        value = i**3
        dict[key] = value
print(dict)



def count_consonant(a):
    vowels = set('aeiou')  # Use a set for faster lookups
    count = 0
    for char in a.lower():  # Convert string to lowercase once
        if char.isalpha() and char not in vowels:  # Check for consonants
            count += 1
    return count
a = input("Enter the string: ")
result = count_consonant(a)
print("Number of consonants:", result)
