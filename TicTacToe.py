def draw_board(): # Draws the initial demonstratory board.
    #Draw board
    print('    1   2   3 ')
    for i in range(3):
        print(str(i+1)+ ' |   |   |   |')
    
def check_winner(b): # Checks to see if there's a winner after every move
    result = True
    
    #check_rows
    for i in range(3):
        row = set([str(b[i][0]), str(b[i][1]), str(b[i][2])])
        if len(row) == 1 and b[i][0] != ' ':
            result = announce_player(b[i][0])
    
    #check_columns
    for i in range(3):
        col = set([str(b[0][i]), str(b[1][i]), str(b[2][i])])
        if len(col) == 1 and b[0][i] != ' ':
            result = announce_player(b[0][i])
        
    #check_diagonals
    diag1 = set([str(b[0][0]), str(b[1][1]), str(b[2][2])])
    diag2 = set([str(b[0][2]), str(b[1][1]), str(b[2][0])])
    if (len(diag1) == 1 or len(diag2) == 1) and b[1][1] != ' ':
        result = announce_player(b[1][1])
    
    return result

def announce_player(winner): # Announces the player who has won the game, if they have.
    if winner == 'X':
        print('\nPLAYER 1 WINS')
    if winner == 'O':
        print('\nPLAYER 2 WINS')
        
    return False
    
def print_real_board(board): # Updates the board with Xs and Os after every move
    print()
    for i in range(3):
        print('| '+' | '.join(board[i])+' |')
    print()            

def check_if_spot_taken(player_choice, board, player_turn): # Checks to see the spot selected is empty so as to not overwrite Xs and Os
    print()
    spot = [int(elem) for elem in player_choice.split(',')]

    while board[spot[0]-1][spot[1]-1] != ' ':
        player_choice = input('That spot is already taken. Please try again player {}.\n'.format(player_turn))
        spot = [int(elem) for elem in player_choice.split(',')]
        
    return spot

print('We are going to use row and column numbers to make moves.')
print('The rows are numbered downwards, from 1 to 3')
print('As the rows, columns are also numbered 1 to 3 left to right')
draw_board()
print("To make a move you'll type in (row,column) to select your spot on the board.")
print("Let's play!\n")

game_on = 0 # Used to keep count of moves, terminating the game when the board is full and no one has won
player_turn = 2 # I used this to initialize the player counter
cont_play = True

board  = [[' ',' ',' '], # This is the array used to map out the TicTacToe using lists.
          [' ',' ',' '],
          [' ',' ',' ']]

while game_on != 9 and cont_play: # Loops as long as the game is active
    #This switches between each player's turn
    if player_turn == 2:  
        player_turn = 1
    else:
        player_turn = 2
        
    # No failsafes here, assumes the players can read and follow instructions and play valid inputs.
    player_choice = input('Make your move player {}.\n'.format(player_turn))
    
    spot = check_if_spot_taken(player_choice, board, player_turn)

    if player_turn == 1:
        board[spot[0]-1][spot[1]-1] = 'X'
    else:
        board[spot[0]-1][spot[1]-1] = 'O'
        
    print_real_board(board)

    cont_play = check_winner(board)

    game_on += 1 

if game_on == 9:
    print('GAME OVER. NO WINNER')
