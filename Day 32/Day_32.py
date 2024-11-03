import random
def game():
    print("You are playing game")
    score = random.randint(1,80)

    with open("highscore.txt") as f:
        highscore = f.read()
        if(highscore != ""):
            highscore = int(highscore)
        else:
            highscore = 0
        
    print(f"Your Score is: {score}")
    if(score>highscore):
        with open("highscore.txt","w") as f:
            f.write(str(score))
game()




def generateTables(n):
    table = ""
    for i in range(1,11):
        table += f"{n} X {i} = {n*i}\n"
    
    with open(f"table_{n}.txt","w") as f:
        f.write(table)


for i in range(2,21):
    generateTables(i)


