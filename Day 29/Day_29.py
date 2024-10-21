n = 5
for i in range(n):
    # Print spaces followed by stars
    print(" " * (n - i - 1) + "*" * (2 * i + 1))


n = 5
for i in range(n):
    if i == 0 or i == n-1:
        print("{}".format("x_"*n))
    else:
        print("*{}*_".format("_"*(2*n-3)))



a = int(input("Enter a number: "))
for num in range(a, 20):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, "is a prime number")


n = 5
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()



