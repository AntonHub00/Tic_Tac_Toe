import os

#Functions --------------------------------------------------------------------------------------------------

#Print the board with the update for the position choosen
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
    \n''')

#Check whether the position is available or is already choosen
def check_available(position):
    return ' ' == board[position-1]

#Check if the input is correct
def check_input():
    position = int(input('Choose a position: '))

    while(True):
        if position in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            if check_available(position):
                return position
            else:
                position = int(input('Invalid position. That position is already choosen: '))
        else:
            position = int(input('Invalid position. Choose a cell bewteen 1 and 9: '))        

#Insert the marker in the position choosen for the corresponding player        
def insert_marker(position, players_turn):
    if players_turn == player1:
        board[position-1] = 'X'
    else:
        board[position-1] = 'O'    

#Check if sombody has won
def check_for_win():
    #Check horizontal
    if board[0] == board[1] == board[2] and board[0] != ' ':
        return True
    elif board[3] == board[4] == board[5] and board[3] != ' ':
        return True
    elif board[6] == board[7] == board[8] and board[6] != ' ':
        return True
     #Check vertical   
    elif board[0] == board[3] == board[6] and board[0] != ' ':
        return True
    elif board[1] == board[4] == board[7] and board[1] != ' ':
        return True
    elif board[2] == board[5] == board[8] and board[2] != ' ':
        return True
    #Check crossed    
    elif board[0] == board[4] == board[8] and board[0] != ' ':
        return True
    elif board[2] == board[4] == board[6] and board[2] != ' ':
        return True
    else: 
        False

#Change the player's turn for the next iteration
def change_turn(players_turn, player1, player2):
    if players_turn == player1:
        return player2
    else:
        return player1

#End of functions-------------------------------------------------------------------------------------------

print('Welcome to Tic Tac Toe!')
print('\n')

while(True):
    player1 = input('Enter the name of the first player: ')
    player2 = input('Enter the name of the second player: ')
    print('\n')

    print(f'The sign for {player1} is "X" and the sign for {player2} is "O"')
    print('\n')
    input('Enter to continue')
    os.system('clear')

    print('You need to use this board as reference to insert an "X" or "O" in the position you want\n')
    board = ['1','2','3','4','5','6','7','8','9']
    print_board(board)
    input('\nEnter to continue')
    os.system('clear')

    # "board" list keeps "X"s and "O"s
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']       
    players_turn = player1

    #The game starts
    while(' ' in board):
        print(f'{players_turn}\'s turn \n ')
        print_board(board)

        position = check_input()

        insert_marker(position, players_turn)

        if check_for_win():
            os.system('clear')
            print_board(board)
            print(f'{players_turn} has won!\n')
            break

        players_turn = change_turn(players_turn, player1, player2)
                
        os.system('clear')

    if not ' ' in board:
        os.system('clear')
        print_board(board)
        print('Tie!\n')    
    
    answer = input('Press enter to exit or type "yes" to replay: ')
    if not answer == 'yes':
        break
    
    os.system('clear')
    
os.system('clear')