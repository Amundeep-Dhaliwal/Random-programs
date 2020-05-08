#! python3

import random


####################################################################################################

'''

def player_input(): # assign player1 marker and player2 marker
    marker = ''
    while (marker != 'X' or marker != 'O'):
        marker = input('Please pick a marker from \'X\' or \'O\':\n').upper()
        if marker == 'O':
            return ('O', 'X')
        elif marker == 'X':
            return ('X', 'O')



def choose_first(): # randomly choose which player makes the first move
        chosen = random.randint(1,2)
        if chosen == 1:
            return 'Player 1'
        else:
            return 'Player 2'

def display_board(lst): # defines the board
            print(f'  {lst[7]}  |  {lst[8]}  |  {lst[9]}  ')
            print(f'-----------------')
            print(f'  {lst[4]}  |  {lst[5]}  |  {lst[6]}  ')
            print(f'-----------------')
            print(f'  {lst[1]}  |  {lst[2]}  |  {lst[3]}  ')



def space_check(board, position): # check if a space is empty on the board
    return board[position] == ' '

def player_choice(board): # takes the input of where the player wants to put their marker
    position = 0 # place holder value
    while position not in list(range(1,10)) or not space_check(board, position):
        try:
            position = int(input('Please input a number (1-9) to indicate the next move: '))
        except ValueError:
            print('Please input a number between 1 and 9')
            continue
    return position


def full_board_check(board): # checks whether the board is full
    total = 0
    for i in range(1,10):
        if board[i] != ' ':
            total += 1
    if total == 9:
        return True
    else:
        return False

def win_check(board, mark): # checks whether there has been a winner
    return ((board[7] == board [8] == board[9] == mark) or
    (board[7] == board [4] == board[1] == mark) or
    (board[7] == board [5] == board[3] == mark) or
    (board[1] == board [5] == board[9] == mark) or
    (board[1] == board [2] == board[3] == mark) or
    (board[9] == board [6] == board[3] == mark) or
    (board[8] == board [5] == board[2] == mark) or
    (board[4] == board [5] == board[6] == mark))

def place_marker(board, marker, position):
    board[position] = marker

def replay():
    return input('Do you want to play again? ').upper()[0] == 'Y'


print('Welcome to Tic Tac Toe!')


while True:
    theBoard = [' '] *10 # defines the playing board!
    play_game = input('Are you ready to play? (Y/N) ') # asks the player if they are ready to play

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False


    player1_marker, player2_marker = player_input() # multiple assignment
    turn = choose_first()
    print(turn + ' will go first...')


    while game_on:



        #Player 1 Turn
        if turn == 'Player 1':

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have one the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else: # note that else statements are not followed by a condition
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Congratulations! You have one the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'


    if not replay():
        break

print('Out of loop')

'''
#############################################################################



'''


def display_board(a,b):
    print('Available TIC-TAC-TOE\n' + ' moves\n\n   ' +
    a[7]+'|'+a[8]+'|'+a[9]+'        '+b[7]+'|'+b[8]+'|'+b[9]+'\n   '+
    '-----        -----\n   '+
    a[4]+'|'+a[5]+'|'+a[6]+'        '+b[4]+'|'+b[5]+'|'+b[6]+'\n   '+
    '-----        -----\n   '+
    a[1]+'|'+a[2]+'|'+a[3]+'        '+b[1]+'|'+b[2]+'|'+b[3]+'\n')




def place_marker(avail, board, marker, position):
    board[position] = marker
    avail[position] = ' '


def win_check(board, mark): # checks whether there has been a winner
    return ((board[7] == board [8] == board[9] == mark) or
    (board[7] == board [4] == board[1] == mark) or
    (board[7] == board [5] == board[3] == mark) or
    (board[1] == board [5] == board[9] == mark) or
    (board[1] == board [2] == board[3] == mark) or
    (board[9] == board [6] == board[3] == mark) or
    (board[8] == board [5] == board[2] == mark) or
    (board[4] == board [5] == board[6] == mark))


def random_player():
    return random.choice((-1, 1))

def space_check(board,position):
    return board[position] == ' '

def full_board_check(board):
    return ' ' not in board[1:]


def player_choice(board, player): # takes the input of where the player wants to put their marker
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        try:
            position = int(input(f'{player} please input a number (1-9) to indicate your next move: '))
        except ValueError:
            print('Please input a number between 1 and 9')
            continue
    return position

def replay():
    permission = input('Do you want to play again? ').upper().startswith('Y')
    if permission  == True:
        #print('\n'*100)
        return True
    else:
        return input('Are you sure? ').upper().startswith('N')



theBoard = [' '] *10 # defines the playing board!
available = [str(num) for num in range(0,10)]
players = [0, 'X', 'O']

while True:
    print('Welcome to Tic Tac Toe!')

    toggle = random_player()
    player = players[toggle] ### THIS IS NEW (potientally game changing?)
    print(f'For this round, player {player} will go first!')

    game_on = True
    input('Hit enter to continue\n')
    while game_on:
        display_board(available, theBoard)
        position = player_choice(theBoard,player)
        place_marker(available, theBoard,player, position)

        if win_check(theBoard, player):
            display_board(available, theBoard)
            print('Congratulations! Player ' + player +' wins!')
            game_on = False
        elif full_board_check(theBoard):
            display_board(available, theBoard)
            print('The game is a tie!')
            game_on= False
        else:
            toggle *= -1
            player = players[toggle]

    theBoard = [' '] * 10
    available = [str(num) for num in range(0,10)]

    if not replay():
        break

'''


#######################################################################################################



def get_board(m, a):
    print('Here is the board\n\n')
    print('          '+a[7] +'|'+ a[8] +'|'+ a[9]+'        '+m[7]+'|'+m[8]+'|'+m[9])
    print('          '+'-----        -----')
    print('          '+a[4] +'|'+ a[5] +'|'+ a[6]+'        '+m[4]+'|'+m[5]+'|'+m[6])
    print('          '+'-----        -----')
    print('          '+a[1] +'|'+ a[2] +'|'+ a[3]+'        '+m[1]+'|'+m[2]+'|'+m[3]+'\n')


def player_input():
    marking = False
    while not marking:
        choice = input('What marking would you like? (X/O) ').upper()
        if choice == 'X':
            return ('X','O')
        elif choice == 'O':
            return ('O','X')
        else:
            continue


def place_mark(board, position, player_mark, available):
    board[position] = player_mark
    available[position] = ' '


def win_check(board, mark):
    return ((board[7] == board[8] == board[9] == mark) or
    (board[4] == board[5] == board[6] == mark) or
    (board[1] == board[2] == board[3] == mark) or
    (board[8] == board[5] == board[2] == mark) or
    (board[9] == board[6] == board[3] == mark) or
    (board[7] == board[4] == board[1] == mark) or
    (board[7] == board[5] == board[3] == mark) or
    (board[9] == board[5] == board[1] == mark))



def turn():
    return random.choice((-1,1))



def full_board(board):
    return ' ' not in board[1:] # remember the board list is [' '] * 10




def space_check(board, position):
    return board[position] == ' '


def mark_placer(board, marker):
    position = 0
    while position not in list(range(1,10)) or not space_check(board, position):
        try:
            position = int(input(f'Where do you place your mark {marker}? (1-9) '))
        except ValueError:
            print('Please enter a number between 1 and 9')
            continue
    return position




def replay():
    choice = input('Do you want to play again? (Y/N) ').lower().startswith('y')
    if choice:
        return True
    else:
        return input('Are you sure? (Y/N) ').lower().startswith('n')



players = [0, 'X', 'O']

while True:
    print('Welcome to Tic Tac Toe!')
    toggle = turn()
    player = players[toggle]
    permission = input('Are you ready to play? (Y/N) ').lower().startswith('n')
    if permission:
        break

    theboard = [' '] *10
    available = [str(x) for x in range(10)]
    print(f'Alright {player} will go first!')


    while True:
        get_board(theboard, available)
        move = mark_placer(theboard, player)
        place_mark(theboard, move, player, available)

        if win_check(theboard, player):
            get_board(theboard, available)
            print(f'Congratulations! {player} has won the game!')
            break

        elif full_board(theboard):
            get_board(theboard, available)
            print('It\'s a tie!')
            break

        else:
            toggle *= -1
            player = players[toggle]


    if not replay():
        break


print('See you starside...')










