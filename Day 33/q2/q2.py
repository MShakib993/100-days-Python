import random
def game():
    print("You are playing game")
    score = random.randint(1,80)

    with open("q2/highscore.txt") as f:
        highscore = f.read()
        if (highscore != ""):
            highscore = int(highscore)
        else:
            highscore = 0
    
    print(f"Your Score: {score}")
    if(score>highscore):
        with open("q2/highscore.txt","w") as f:
            f.write(str(score))
game()
