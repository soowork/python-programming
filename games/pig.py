import random

'''
def play_pig():
    player1_score, player2_score = 0, 0

    # player1 will be 0, player2 will be 1
    turn = random.randint(0,1) 

    # do while neither player has reached a score of 10 
    while(True):
        # condition for exiting will be in the while loop

        # if it is player1's turn we are going to roll or hold (s/he is 0)
        if turn == 0:
            choice = input('[PLAYER 1] Roll (r) or Hold (h): ')
            if choice == 'r':
                turn_score = random.randint(1,6)
                # if player rolls 1, score goes to 0 and turn goes to next player
                if turn_score == 1:
                    player1_score = 0 
                    turn = 1 
                else:
                    player1_score += turn_score
                print(f"roll is {turn_score}, and total is {player1_score}")
            else:
                # player has chosen to hold
                # score is unchanged - turn changes
                turn = 1

        if turn == 1:
            choice = input('[PLAYER 2] Roll (r) or Hold (h): ')
            if choice == 'r':
                turn_score = random.randint(1,6)
                # if player rolls 1, score goes to 0 and turn goes to next player
                if turn_score == 1:
                    player2_score = 0 
                    turn = 0 
                else:
                    player2_score += turn_score
                print(f'roll is {turn_score}, and total is {player2_score}')
            else:
                # player has chosen to hold
                # score is unchanged - turn changes
                turn = 0

        # check to see if anyone has won
        if player1_score >= 10 or player2_score >= 10:
            break

    # print the name of the winner
    if player1_score >= 10:
        print("PLAYER 1 WINS!")
    else:
        print("PLAYER 2 WINS!")
    

play_pig()  
'''

# this is refactor - we didn't get it quite working yet 
player_scores = [0,0]
turn = random.randint(0,1)
def roll(turn):
    choice = input(f'[PLAYER {turn+1}] Roll (r) or Hold (h): ')
    if choice == 'r':
        turn_score = random.randint(1,6)
        # if player rolls 1, score goes to 0 and turn goes to next player
        if turn_score == 1:
            player_scores[turn] = 0 
            turn = abs(turn-1)
        else:
            player_scores[turn] += turn_score
        print(f"roll is {turn_score}, and total is {player_scores[turn]}")
    else:
        # player has chosen to hold
        # score is unchanged - turn changes
        turn = abs(turn-1)


while(True):
    roll(turn)
    if player_scores[0] >= 20 or player_scores[1] >= 20:
        break

if player_scores[0] >= 20:
    print("PLAYER 1 WINS!")
else:
    print("PLAYER 2 WINS!")



