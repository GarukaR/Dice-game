import random
#to welcome the player
print('Welcome to the Pig Dice Game')

#get the number of player
no_player=int(input('Enter the number of players (1 to 4) :  '))

#display the rules for the gameplay
print('Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to \"hold\":')
print('\t 1)If the player rolls a 1, they score nothing and it becomes the next player\'s turn.')
print('\t 2)If the player rolls any other number, it is added to their turn total and the player\'s turn continues.')
print('\t 3)If a player chooses to "hold", their turn total is added to their score, and it becomes the next player\'s turn.')
print('The first player to score 100 or more points wins.')

#list is created to store the score for each player
players_score=[]

#initial score is set to ZERO for each player
for count in range(0,no_player):
    players_score.append(0)
    
input('Press enter to start the game')

#to roll single until an winner is emerged
count=0
winner_found=False
while winner_found!=True:
    hold=None
    turn_score=0
    # for each player allowed to play until 1 is scored or player decides to hold
    while hold != 'y':
        result=random.randint(1,6)#single die is rolled
        print('Rolling the dice for player ',count+1,'...',result)#result of the die is displayed
        if result == 1:#if the score of rolled die is 1 then turn score and overall score for that player
                       #becomes ZERO and the chance given to the next player to roll the die 
            turn_score=0
            players_score[count]=0
            hold='y'
        else:#if the score of rolled die is other than ZERO then added to turn score
             #Also player is asked whether to hold or continue to roll the die
            turn_score+=result
            hold=input('Do you want to hold(\'y\')continue(\'n\') : ').lower()
            if hold == 'y':
                players_score[count]+=turn_score
    #end of the turn the overall score is displayed to user            
    print('the score of player ',count+1,' is ',players_score[count])

    #if the last player scored 100 or more the game stops and winner details are displayed            
    if players_score[count] >= 100:
        winner_found=True
        print('the winner is player ',count+1,' with the score of ',players_score[count])
    else:
        input('Press enter to roll the for the next player ')
    count+=1#to increase the player no by one
    count%=no_player# if the player no reaches no of player then reset to 1
           
    
    
    
    
    
