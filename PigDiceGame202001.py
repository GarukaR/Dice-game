import random

def get_player():
    print('Welcome to the dice game')
    valid_input = 'N'
    while valid_input == 'N':
        no_player = int(input('Enter the number of player (1..4) : '))
        if no_player > 4 or no_player < 1:
            print('Invalid number of player enter a value between 1 to 4')
            valid_input = 'N'
        else:
            valid_input = 'Y'

    return no_player

def display_rules():
    print('How to play the pig dice game')
    print('___________________________________________________________________________________________________________________')    
    print('Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to \"hold\":')
    print('\t If the player rolls a 1, they score nothing and it becomes the next player\'s turn.')
    print('\t If the player rolls any other number, it is added to their turn total and the player\'s turn continues.')
    print('\t If a player chooses to "hold", their turn total is added to their score, and it becomes the next player\'s turn.')
    print('The first player to score 100 or more points wins.')
    print('___________________________________________________________________________________________________________________')

def set_initial_score(scores, no_player):
    for count in range(0,no_player):
        scores.append(0)
    
def find_winner(no_player):
    scores=[]

    set_initial_score(scores, no_player)
    player=0
    stop='N'
    while stop == 'N':

        score=random.randint(1, 6)
        print('the player with the index ', player, 'rolled : ', score)
        scores[player]+=score
        if score == 1:
            scores[player] = 0
            print('The player with the index ', player, ' set to zero and the next player will be given the change ')
            player += 1
            player = player % no_player
        else:
            answer=input('Do you want hold press \'Y\' or to continue press any other key : ')
            if answer == 'Y' or answer == 'y':
                print('the player with the index ', player, ' has scored : ', scores[player])
                player += 1
                player %= no_player
                print('The player with the index ', player,'will be continue to play')

        if scores[player] >= 20:
            print('The winner is found the player with the index ',player,'is the winner and the score is ', scores[player])
            ans=input('Winner found do you wish to play again press \'Y\' or to stop press any other key : ')
            if ans == 'Y' or ans == 'y':
                player=0
                set_initial_score(scores, no_player)
                print('-------------------------------------------------------------------------------')
                print('--------------------------------New Game Starts--------------------------------')
            else:
                print('Bye bye the game ends')
                stop = 'Y'
                 
             
    
number=get_player()
display_rules()
find_winner(number)
