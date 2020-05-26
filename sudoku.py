"""

# 2D list of lists
play = [
    [3,0,7,5,0,0,2,6,1],
    [0,8,0,0,2,0,0,0,0],
    [2,5,0,0,1,0,0,0,0],
    [0,3,0,4,0,5,0,7,2],
    [0,0,8,0,0,0,5,1,0],
    [0,0,5,0,0,0,9,3,0],
    [0,0,0,7,5,0,3,0,6],
    [8,0,0,2,3,0,0,4,0],
    [0,0,3,8,0,4,0,2,9]
    ]

def print_board(board):
    '''
    prints the board
    :param board: 2d list of integers
    :return: None
    '''
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('-----------------------')
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(' | ', end= '')

            if j == 8:
                print(board[i][j], end = '\n')
            else:
                print(str(board[i][j]) + ' ', end = '')





def find_empty(board):
    '''
    finds a empty space in the board
    :param board: partially complete board
    :return: (int row,int col) row col
    '''

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # tuple of row and column

    return None





def valid(board, position, num):
    '''
    returns if attempted move is valid
    :param board: 2d list of integers
    :param pos: (row, col) tuple of (x, y) form
    :param num: integer
    :return: bool
    '''

    # check row
    for i in range(0, len(board)):
        if board[position[1]][i] == num:
            return False

    #check col
    for i in range(0, len(board)):
        if board[i][position[0]] == num:
            return False

    # check box
    box_x = position[1]//3
    box_y = position[0]//3

    for i in range(box_y*3, box_y*3 +3):
        for j in range(box_x*3, box_x*3 +3):
            if board[i][j] == num:
                return False

    return True


def solve(board):
    '''
    solves sudoku board using back tracking
    :parameter board: is a 2d list of integers
    :return: solution
    '''
    find = find_empty(board)
    if find:
        row, col = find
    else:
        return True

    for i in range(1,10):
        if valid(board, (row,col), i):
            board[row][col] = i

            if solve(board):
                return True
    return False




solve(play)
print_board(play)

"""
"""

import numpy
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
    ]

print(numpy.matrix(board))

def possible(x,y,num):
    global board
    for i in range(0,9):
        if board[i][y] == num:
            return False
    for j in range(9):
        if board[x][j] == num:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(3):
        for j in range(3):
            if board[x0+i][y0+j] == num:
                return False
    return True


def solve():
    global board
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                for num in range(1,10):
                    if possible(y,x,num):
                        board[y][x] == num
                        solve()
                        board[y][x] = 0
                return
    print(numpy.matrix(grid))
    input('More?')

solve()
"""


def possible(i,j,z):
    '''
    i is an integer
    j is an integer
    z is the chosen integer
    '''
    #if board.shape!=(9,9):  checks the dimensions of the board are correct
        #raise(Exception("Sudokumatrix not valid"));
    global board
    if 8 < i < 0:
        raise(Exception("i not valid"));
    if 8 < j < 0:
        raise(Exception("j not valid"));
    if 9 < z < 1:
        raise(Exception("z not valid"));

    if(board[i][j]!=0):
        return False;

    for x in range(0,9):
        if(board[x][j]==z):
            return False;

    for y in range(0,9):
        if(board[i][y]==z):
            return False;

    row = int(i/3) * 3;
    col = int(j/3) * 3;
    for ii in range(0,3):
        for jj in range(0,3):
            if(board[ii+row][jj+col]==z):
                return False;

    return True;

def print_board(board):
    '''
    prints the board
    :param board: 2d list of integers
    :return: None
    '''
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('-----------------------')
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(' | ', end= '')

            if j == 8:
                print(board[i][j], end = '\n')
            else:
                print(str(board[i][j]) + ' ', end = '')

def possibleNums(i ,j):
    '''
    returns a list of numbers that could go in board[i][j]
    '''
    potential = []
    ind = 0
    for k in range(1,10):
        if possible(i,j,k):
            potential.insert(ind,k)
            ind+=1
    return potential

def solve(board):
    zeroFound = 0;
    for i in range(9):
        for j in range(9):
            if(board[i][j]==0):
                zeroFound=1;
                break;
        if(zeroFound==1):
            break;
    if(zeroFound==0):
        print("The solution I came up with: ")
        empty = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
        ]
        for x in range(9):
            for y in range(9):
                empty[x][y] = board[x][y]
        print_board(empty)
        return empty


    a_list = possibleNums(i,j)

    for k in range(len(a_list)):
        board[i][j]=a_list[k]
        solve(board)
    board[i][j] = 0


test_board = [
    [4,1,0,0,3,6,0,0,0],
    [0,0,7,0,0,0,8,5,0],
    [6,0,0,0,0,0,0,0,0],
    [0,9,0,0,0,0,2,0,0],
    [0,0,6,0,7,0,0,0,8],
    [0,0,0,0,0,0,0,9,1],
    [0,0,2,0,1,4,0,0,0],
    [0,0,0,0,0,3,0,0,0],
    [7,4,0,0,0,8,5,0,9]
    ]

board = []
while len(board) < 9:
    user_input = (input('Please input the line of 9 numbers: ')).split()
    if len(user_input) != 9:
        continue
    one_d = [int(x) for x in user_input]
    board.append(one_d)
    

print_board(board)
solve(board)
