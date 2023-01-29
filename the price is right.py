import random 
import sys 

x = random.randint(1000, 5000)

def takeClosest(num,collection):
   return min(collection,key=lambda x:abs(x-num))

while True:
    try:
        player1 = int(input("Player 1, what is your bid? "))
        player2 = int(input("Player 2, what is your bid? "))
        player3 = int(input("Player 3, what is your bid? "))
        player4 = int(input("Player 4, what is your bid? "))
        break
    except ValueError:
        continue 
    else:
        break 

player_values = [player1, player2, player3, player4]
player_order = {player1 : "Player 1", player2 : "Player 2", player3 : "Player 3", player4 : "Player 4"}
for player in player_values:
    if player in player_order:
        if player1 > x and player2 > x and player3 > x and player4 > x:
            sys.exit("Buzz! Aww... everyone has overbid!")
        elif player == x:
            print("Ding Ding Ding! One player got it exactly right and gets $500!")
            print(f"Actual price is ${x}! {player_order[player]}, come on up! ")
        elif player == takeClosest(x, player_values):
            sys.exit(f"Actual price is ${x}! {player_order[player]}, come on up!")




