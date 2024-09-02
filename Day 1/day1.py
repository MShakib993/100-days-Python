# String method 

var = "sHaKib"
print(len(var))
print(var.endswith("ib"))
print(var.count("i"))

b = var.capitalize()
print(b)

c = var.upper()
print(c)

d = var.lower()
print(d)


e = var.replace("sHaKib" , "Babul")
print(e)

f = e.find("b")
print(f)

a = 123
b = (str(a))
print(type(b))

print("Sha\nkib")
print("Sha\tkib")
print("Sha\\kib")
print("Sha\'kib")


hello = "Hello World"
print(hello[0: ])
print(hello[ :-1 ])
print(hello[ : ])
print(hello[ :-1:1])
print(hello[ :-1:2])

print(hello.split())



s = "Hello eWorld"
print(s.index("World"))  # Output: 6

words = ["Hello", "World"]
print(" ".join(words))  # Output: "Hello World"

