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

print('You need to use this board as reference to insert an "X" or "O" in the position you want\n')
board = ['1','2','3','4','5','6','7','8','9']
print_board(board)
input('\nEnter to continue')
os.system('clear')

# "board" list keeps "X"s and "O"s
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

#check whether the position is available or is already choosen
def check_available(position):
    return ' ' == board[position-1]

#Check if sombody has won
def check_for_win():
    x_win= ['X','X','X']
    o_win= ['O','O','O']

    if board[:3] == x_win  or board[3:6] == x_win or board[6:] == x_win: #Horizontal Check for X and O
        return True
    elif board[:3] == o_win  or board[3:6] == o_win or board[6:] == o_win:
        return True
    elif [x for x in board[::3]] == x_win  or [x for x in board[1::3]] == x_win or [x for x in board[2::3]] == x_win: #Vertical Check for X and O
        return True
    elif [x for x in board[::3]] == o_win  or [x for x in board[1::3]] == o_win or [x for x in board[2::3]] == o_win:
        return True
    elif [x for x in board[::4]] == x_win or [x for x in board[::4]] == o_win: #Crossed check for X and O
        return True
    elif [x for x in board[2:8:2]] == x_win or [x for x in board[2:8:2]] == o_win:
        return True
    else:
        return False

players_turn = player1

while(' ' in board):
    print(f'{players_turn}\'s turn \n ')
    print_board(board)

    position = int(input('Choose a position: '))

    while(True):
        if check_available(position):
            break
        else:
            position = int(input('That position is already choosen. Choose another position: '))

    #Set the X or O in the cell
    if players_turn == player1:
        board[position-1] = 'X'
    else:
        board[position-1] = 'O'

    if check_for_win():
        break
    #Changing player before the next iteration
    if players_turn == player1:
        players_turn = player2
    else:
        players_turn = player1
            
    os.system('clear')

os.system('clear')
print_board(board)

if ' ' in board:
    print(f'{players_turn} has win!')
else:
    if check_for_win():
        print(f'{players_turn} has win!')
    else:
        print('Nobody has won :c')    
    