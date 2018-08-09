import os

print('Welcome to Tic Tac Toe!')
print('\n')

player1 = input('Enter the name of the first player: ')
player2 = input('Enter the name of the second player: ')
print('\n')

print(f'The sign for {player1} is "X" and the sign for {player2} is "O"')
print('\n')
input('Enter to continue')
os.system('clear')

board = ['1','2','3','4','5','6','7','8','9']

def print_board(board):
    print(f'''
     |     |     
  {board[6]}  |  {board[7]}  |  {board[8]}  
     |     |     
-----------------
     |     |     
  {board[3]}  |  {board[4]}  |  {board[5]}  
     |     |     
-----------------
     |     |     
  {board[0]}  |  {board[1]}  |  {board[2]}  
     |     |     
    ''')

print('You need to use this reference to insert an "X" or "O" in the position you want\n')
print_board(board)
input('\nEnter to continue')
os.system('clear')

# "board" list keeps "X"s and "O"s
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

def cheak_available(position):
    return ' ' == board[position-1]

players_turn = player1
while(' ' in board):
    print(f'{players_turn}\'s turn \n ')
    print_board(board)

    position = int(input('Choose a position: '))

    while(True):
        #check whether the position is available or is already choosen
        if cheak_available(position):
            break
        else:
            position = int(input('That position is already choosen. Choose another position: '))

    #Set the X or O in the cell
    if players_turn == player1:
        board[position-1] = 'X'
    else:
        board[position-1] = 'O'

    if players_turn == player1:
        players_turn = player2
    else:
        players_turn = player1
            
    os.system('clear')

print_board(board)