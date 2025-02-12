#Create and display the board: Use a 3x3 2D list to represent the game board and display it after every turn. Using a fuction to print the state of the board.
#Player input: Allow two players to take turns choosing their move.
#Input validation: Ensure that the chosen cell is empty before marking it.
#Check for a winner: Implement a function to determine if a player has won.
#Check for a draw: If all spaces are filled and no winner is found, the game ends in a draw.
#End game: Display the winner or announce a draw, then ask if players want to play again.
#Partner: You will work with 1 other person on this project and you should use GitHub to collaborate.
#Testing: You will test your code with 1 other group to test your code and improve your game.




scores = {'Player1':0, 'Player2':0}
scores['Player1'] += 1
print(scores)

def print_scores(scores):
    print(f"Player 1 score: {scores['Player1']} \nPlayer 2 score: {scores['Player2']}")

print_scores(scores)