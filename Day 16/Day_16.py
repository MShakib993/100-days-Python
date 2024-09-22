num1 = int(input("Enter a num: "))
for i in range(1,num1):
    print(" "* (num1-i),end="")
    print("*"* (2*i-1),end="")
    print()




num1 = int(input("Enter a num: "))
for i in range(1,num1):
    print("*"*i)




num2 = int(input("Enter a num1: "))
for i in range(1,num2+1):
    if(i==1 or i == num2):
        print("*"*num2, end="")
    else:
        print("*",end="")
        print(" "*(num2-2), end="")
        print("*",end="")
    print("")



n = int(input("Enter the number: "))
for i in range(1, n+1): 
    if(i==1 or i==n):
        print("*"* n, end="")
    else:
        print("*", end="")
        print(" "* (n-2), end="")
        print("*", end="")
    print("")


        



        
