import random

def game():
    score = random.randint(1, 100)
    print(f"The score is {score}")
    return score

score = game() #returns certain score to variable score

with open("highscore.txt", "r") as f:
    highscore = int(f.read())
if highscore<score:
    with open("highscore.txt", "w") as f:
        f.write(f"{score}")
else:
    print("You arent able to beat the high score")
        