import random
def main():
    options = ["Rock","Paper","Scissors"]
    comp_choice1 = random.randint(0,2)
    comp_choice2 = random.randint(0,2)
    comp_hands = [options[comp_choice1], options[comp_choice2]]
    player_hand1 = int(input('Rock(1), Paper(2), or scissors(3) for left hand: '))
    player_hand2 = int(input('Rock(1), Paper(2), or scissors(3) for right hand: )'))
    if player_hand1 == 1:
        print("Your left hand is Rock!")
        player_hand1 == "Rock"
    elif player_hand1 == 2:
        player_hand1 == "Paper"
        print("Your left hand is Paper!")
    elif player_hand1 == 3:
        player_hand1 == "Scissors"
        print('Your left hand is Scissors!')
    else: 
        print('Play the game right')
    if player_hand2 == 1:
        player_hand2 == "Rock"
        print(f'Your right hand is {player_hand2}!')
    elif player_hand2 == 2:
        player_hand2 == "Paper"
        print('Your right hand is Paper!')
    elif player_hand2 == 3:
        player_hand2 == "Scissors"
        print('Your right hand is Scissors!')
    else:
        print('Play the game right')
    print(f'The computer chose {comp_hands}')
    remove_hand = input(f"Which hand do you want to remove, Right{player_hand2} or Left{player_hand1}: ")
    if remove_hand.lower() == "right":
        print(f"You removed your {remove_hand} hand!")
    
main()