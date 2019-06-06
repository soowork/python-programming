import random
player_total = 0
player2_total = 0
player1_total = 0

def turn(player,player_total):
    choice = input("Press r or h: ")
    if choice == "r":
        roll = random.randint(1,6)
        print("roll is",roll)
        if roll == 1:
            player_total = 0
        else:
            player_total += roll
        #elif choice == "h":
        # no action required
    return player_total

while not( player1_total >= 30 or player2_total >= 30):
    player1_total = turn("player1 ", player1_total)
    print("player1 total ",player1_total)
    
    if player1_total >= 30:  
        print("game is over! player1 dominated")
    else: 
        player2_total = turn("player2 ", player2_total)
        print("player2 total ",player2_total)
        if player2_total >= 30:  
            print("game is over! player2 rules!")
