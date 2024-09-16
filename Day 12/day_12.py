frmt1 = "Welcome to {name} in {college}".format(name="Coding Block",college="LPU")
print(frmt1)

frmt2 = "Welcome to {0} in {1}".format("Coding block","LPU")
print(frmt2)

frmt3 = "Welcome to {} in {}".format("Coding Block","LPU")
print(frmt3)

frmt4 = "Welcome to {a:^10} in {b:>10}".format(a="sk",b="LPU")
print(frmt4)


n = 5
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()






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
