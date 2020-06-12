import platform
from os import system
from time import sleep

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

# This checks to see if the board is solved or not, and if it isn't, it tries to solve it recursively
def solver(bd):
    if not empty_spot(bd):
        return True
        
    else:
        x, y = empty_spot(bd)
        for i in range(1, 10):
            if valid_move((x, y), i, bd):
                bd[x][y] = i
                print_board(bd)
                sleep(0.2)
                clear_screen()
                if solver(bd):
                    return True
                
                bd[x][y] = 0
                print_board(bd)
                sleep(0.2)
                clear_screen()
                
        return False


# This checks if a move is valid or not
def valid_move(move, val, bd):
# Checks row
    for i in range(len(bd)):
        if bd[i][move[1]] == val and move[0] != i:
            return False
# Checks column
    for i in range(len(bd[0])):
        if bd[move[0]][i] == val and move[1] != i:
            return False

# Checks individual 3x3 grids
    grid_column = move[1] // 3
    grid_row = move[0] // 3
    
    for i in range(grid_row * 3, grid_row * 3 + 3):
        for j in range(grid_column * 3, grid_column * 3 + 3):
            if bd[i][j] == val and (i, j) != move:
                return False
            
    return True
  
# Checks if a spot is empty or not and if it is, it returns the position as a tuple
def empty_spot(bd):
    for i in range(len(bd)):
        for j in range(len(bd[0])):
            if bd[i][j] == 0:
                return (i, j)
            
    return False

# Clears the screen 
def clear_screen():
    if 'windows' in platform.system().lower():
        system('cls')
    else:
        system('clear')

# Prints the board
def print_board(bd):
    for i in range(len(bd)):
       if i % 3 == 0 and i != 0:
           print('- - - - - - - - - - -')
    
       for j in range(len(bd[0])):
           if j % 3 == 0 and j != 0:
               print('| ', end = '')
                
           if j == (len(bd[0]) - 1):
               print(bd[i][j])
           else:
               print(str(bd[i][j]) + ' ', end = '')
            
   
print_board(board)   
solver(board)
sleep(0.2)
clear_screen()
print_board(board)  
