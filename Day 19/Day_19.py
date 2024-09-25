n = int(input("enter a num1: "))
def factorial(g):
    if g==1 or g==0:
        return 1
    return g * factorial(g-1)
print(f"The factorial of n is,{factorial(n)}")


def greatest(a,b,c):
    if(a>b and a>c):
        print(a)
    elif(b>a and b>c):
        print(b)
    else:
        print(c)
    
d = int(input("Enter the num1: "))
e = int(input("Enter the num1: "))
f = int(input("Enter the num1: "))

greatest(d,e,f)


fern = int(input("Enter a num: "))
def fern_to_cel(f):
    return 5*(f - 32)/9
c = fern_to_cel(fern)
print(f"The value is {round(c,2)}C")

