# post = input("Write something: ")
# if("harry" in post.lower()):
#     print("This is talking about harry")
# else:
#     print("This is not talking about harry")


# p1 = "Shakib"
# p2 = "Zamin"
# p3 = "Mithi"
# p4 = "EKsha"
# message = input("Write something: ")
# if(p1 in message or p2 in message or p3 in message or p4 in message):
#     print("This is spam")
# else:
#     print("clear")


# ff = 5
# for ff in range(10):
#     print(ff)

# i = 0
# while(i<5):
#     print("Shakib")
#     i+=1



# dd = ["Shakib","Mithi","Babul","Eksha","Zamin"]
# for item in dd:
#     print(item)
# else:
#     print("End")

# cc =0
# while(cc<len(dd)):
#     print(dd[cc])
#     cc+=1


table = int(input("Write a num: "))
for i in range(1,11):
    print(f"{table} X {i} = {table*i}")



list1 = ["Shakib","Shubham","Sneha","Shreya"]
for name in list1:
    if(name.startswith("S")):
        print(name)  