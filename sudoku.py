
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
