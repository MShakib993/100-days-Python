def add(*pp):
    return sum(pp)

print(add(8, 6, 5, 4, 3, 6)) 


def multiply(*pp):
    result = 1
    for num in pp:
        result *= num
    return result

print(multiply(8, 6, 5, 4, 3, 6))



def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

# Example usage:
my_function(name="Alice", age=25, language="Python")


def my_function(*args):
    for arg in args:
        print(arg)

# Example usage:
my_function(1, 2, 3, "Python")


a = "My Name is Md Shakib"
b = a.split(",")
print(b)


c = ["My","Name","is","Md","Shakib"]
d = " ".join(c)
print(d)


def my_fun(*args):
    for arg in args:
        print(arg)
my_fun(1,2,3,"python")


def fun(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} = {value}")
fun(name = "Shakib", age = 25 , lang = "english")
