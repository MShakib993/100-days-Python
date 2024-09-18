n = int(input("Enter a number: "))

for i in range(2, n):
    if(n%i) == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")



n = int(input("Enter the number: "))
i = 1
sum = 0
while(i<=n):
    sum += i
    i+=1

print(sum)