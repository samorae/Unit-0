import random
def main():
    options = ["rock","paper","scissors"]
    comp_choice1 = random.randint(0,2)
    comp_choice2 = random.randint(0,2)
    comp_hands = [options[comp_choice1], options[comp_choice2]]
    player_hand1 = int(input('Rock(1), Paper(2), or scissors(3) for left hand: '))
    player_hand2 = int(input('Rock(1), Paper(2), or scissors(3) for right hand: )'))
    if player_hand1 == 1:
        print("Your left hand is Rock!")
    elif player_hand1 == 2:
        print("Your left hand is Paper!")
    elif player_hand1 == 3:
        print('Your left hand is Scissors!')
    else: 
        print('Play the game right')
    if player_hand2 == 1:
        print('Your right hand is Rock!')
    elif player_hand2 == 2:
        print('Your right hand is Paper!')
    elif player_hand2 == 3:
        print('Your right hand is Scissors!')
    else:
        print('Play the game right')
    print(f'The computer chose {comp_hands}')
    
main()