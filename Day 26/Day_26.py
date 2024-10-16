f = open("file.txt" , "r")
data = f.read()
print(data)
f.close()


st = "Hey Shakib How are you"
ff = open("myfile.txt" , "w")
ff.write(st)
ff.close()


st1 = "Hey Shakib How are you"
ff1 = open("myfile.txt" , "a")
ff1.write(st1)
ff1.close()


fff = open("file.txt")
liner = fff.readlines()
print(liner, type(liner))
fff.close()


