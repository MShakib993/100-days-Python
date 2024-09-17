def names(a,b):
    print("First name is: ",a)
    print("last name is: ",b)

def ask():
    first_name = input("Enter your name: ")
    last_name = input("Enter your  last name: ")
    names(first_name,last_name)
ask()


n = int(input("Enter a num: "))
i = 1
while(i<11):
    print(f"{n} X {i} = {n*i}")
    i += 1


for i in range(1,11):
    print(f"{n} X {i} = {n*i}")


num = int(input("Enter a num: "))
for i in range(2,num):
    if(n%i)==0:
        print("It is not prime")
        break
    else:
        print("It is prime num")


