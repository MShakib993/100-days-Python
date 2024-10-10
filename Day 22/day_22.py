import random
computer = random.choice([-1,0,1])
youstr = input("Enter your choice s for snake w for water g for gun: ")
youdict = {
    "s" : 1,
    "w" : -1,
    "g" : 0
}

reversedict = {
    1 : "snake",
    -1 : "water",
    0 : "gun"
}

you = youdict[youstr]
if computer == you:
    print("You both choose same It's draw")
else:
    if (computer == 1 and you == -1):
        print("You Loose")
    elif (computer == -1 and you == 1):
        print("You Win")
    elif (computer == 1 and you == 0):
        print("You win")
    elif (computer == 0 and you == 1):
        print("You Loose")
    elif (computer == -1 and you == 0):
        print("You Loose")
    elif (computer == 0  and you == -1):
        print("You win")
    else:
        print("invalid input")
    
print(f"You Choose {reversedict[you]}\ncomputer choose {reversedict[computer]}")