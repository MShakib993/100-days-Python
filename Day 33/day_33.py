a = int(input("Enter a num: "))
b = int(input("Enter a num: "))

try:
    print(a/b)
except Exception as e:
    print("Invalid input ",e)

print(a+b)
print(a-b)



try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
    
except IndexError:
  print("Index Error")


  