import random

def game_win(computer, user):
    if computer == user:
        return None
    if computer == "s" and user == "w":
        return False
    if computer == "s" and user == "g":
        return True
    
    if computer == "w" and user =="s":
        return True
    if computer == "w" and user == "g":
        return False
    
    if computer == "g" and user == "s":
        return False
    if computer == "g" and user == "w":
        return True

rand_no = random.randint(1,3)
print("Computer's turn: Snake(s), Water(w), Gun(g)?")

if rand_no == 1:
    computer = "s"
elif rand_no == 2:
    computer = "w"
else:
    computer = "g"


user = input("your turn: Snake(s), Water(w), Gun(g)?").lower()

result = game_win(user,computer)
print(f"You chose {user}")
print(f"Computer chose {computer}")

if result == None:
    print("The game is a tie!")
elif result:
    print("You win!")
else:    print("You lose!")