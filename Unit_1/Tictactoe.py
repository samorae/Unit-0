#Create and display the board: Use a 3x3 2D list to represent the game board and display it after every turn. Using a fuction to print the state of the board.
#Player input: Allow two players to take turns choosing their move.
#Input validation: Ensure that the chosen cell is empty before marking it.
#Check for a winner: Implement a function to determine if a player has won.
#Check for a draw: If all spaces are filled and no winner is found, the game ends in a draw.
#End game: Display the winner or announce a draw, then ask if players want to play again.
#Partner: You will work with 1 other person on this project and you should use GitHub to collaborate.
#Testing: You will test your code with 1 other group to test your code and improve your game.
player_1 = 'X'
player_2 = 'O'
placement_guide={
1: (0,0), 
2: (0,1),
3: (0,2),
4: (1,0),
5: (1,1),
6: (1,2),
7: (2,0),
8: (2,1),
9: (2,2)
}

def create_board():
    board = [
        ["1 |","2 |","3"],
        ["4 |","5 |","6"],
        ["7 |","8 |","9"]]
    for row in board:
        for item in row:
            print(item,end=" ")
        print()
    print()
    return board
def move(player_1, player_2, board,):
    user_move = int(input(f'Start player one: Where would your like to place your {player_1}?: '))
    location = placement_guide[user_move] # returns (row, col)
    board[row][col] = player_1
    return board
def user_scores():
    scores = {'Player1':0, 'Player2':0}
    print(scores)

def print_scores(scores):
    print(f"Player 1 score: {scores['Player1']} \nPlayer 2 score: {scores['Player2']}")
def main():
    board = create_board()
    board = move(player_1,player_2,board)
    print(board)

main()