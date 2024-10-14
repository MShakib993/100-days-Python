def nameage(*,name,age):
    print(name,age)
nameage(age=6,name="Shakib")


def namecityage(name , * , age , city):
    print(f"My name is {name} and My age is {age} and I am from {city}")
namecityage("Shakib",age=8,city="Katihar")


def cube(x):
    return x*x*x

l = [1,2,3,4,5,6]
newl = list(map(cube,l))
newl = list(map(cube,l))
print(newl)

newl1 = list(map(cube,l))
print(newl1)


def filter_fun(a):
    return a>4
newl2 = list(filter(filter_fun,newl1))
newl2 = list(filter(filter_fun,l))
print(newl2)

from functools import reduce
numbers = [1,2,3,4,5,6,7,8]
def mysum(x,y):
    return x+y
sum = reduce(mysum,numbers)
print(sum)