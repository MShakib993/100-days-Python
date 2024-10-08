def fun1(n):
    sum = 0
    for i in range(1,n + 1):
        sum += i
    return sum
print(fun1(5))

def fun1(n):
    if n ==1:
        return 1
    return n+fun1(n-1)
print(fun1(5))

def fun1(n):
    if n ==1:
        return 1
    return n*fun1(n-1)
print(fun1(5))


def sum(n):
    if n == 0:
        return 0
    a = n%10
    n = n//10
    return a+sum(n)
print(sum(5568))

def fun(n):
    if n == 0:
        return 0
    return n%10 + fun(n//10)
print(fun(4567))