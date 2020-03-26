# Niranjan prof

#https://github.com/Niranjanprof
#Mailme @ niranjannb7777@gmail.com

# Rock Paper Scissors


import random
def name_check(name):                      #  to check player name
    if (name.strip() == ""):
        return "Guest"
    return name
def disp_hand(name,hand):                   # to print the corresponding moves by player and computer
    hands=['Rock','Paper','Scissors']
    print(name+" picked "+hands[hand])
def judge(player,computer):                 # to Judge the winner
    if( player==computer ):
        return 'Draw'
    elif player == 0 and computer == 1 or player == 1 and computer == 2 or player == 2 and computer == 0:
        return  'Lose'
    else:
        return 'Win'
def validate(hand):                         # to validate user entry regarding the moves
    if  0<=hand<=2:
       return True
    print("\n*******Wrong Input*******\n")
    return False
while(True):
    print("The Rock Paper Scissors Game is Starting")
    player_name=input("Enter your name: ")
    player_name = name_check(player_name)
    print("Hey "+player_name)
    while(True):
        try:
            player_hand=int(input("1:Rock\n2:Paper\n3:Scissors\nEnter your Choice(1/2/3): "))
        except ValueError:
            print("\n*******Wrong Input*******\n")
        else:
            player_hand -= 1
            if validate(player_hand):
                break
    computer_hand=random.randint(0,2)
    disp_hand(player_name,player_hand)
    disp_hand('Computer',computer_hand)
    print("Result: "+judge(player_hand,computer_hand))
    flag = input("Press 1 for playing again ********* Press anything else to exit: ")
    print("**************************************************************************")
    if flag !='1':
        break
