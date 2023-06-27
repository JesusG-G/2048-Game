import random

#Function to add a random 2 to the matrix
def add_new_2(matriz):
    random_row = random.randint(0,3)
    random_column = random.randint(0,3)

    while matriz[random_row][random_column] !=0:
        random_row = random.randint(0,3)
        random_column = random.randint(0,3)

    matriz[random_row][random_column] = 2

#Function to start the game and create the matrix
def start_game():
    print("2048 GAME")
    print("""
    Commands are as follows : 
    'W' or 'w' : Move Up
    'S' or 's' : Move Down
    'A' or 'a' : Move Left
    'D' or 'd' : Move Right 
    """)
    matriz = []
    for _ in range(4):
        matriz.append([0]*4)
    add_new_2(matriz)
    return matriz
#Function to get the current state of the matrix
def get_current_state(matriz):
    status = "YOU LOST"

#if there a 2048 on some position you won
    for i in range(4):
        for j in range(4):
            if matriz[i][j] == 2048:
                status = 'YOU WON'
#if there a zero on the matrix on some position the game is not over
    for i in range(4):
        for j in range(4):
            if matriz[i][j] == 0:
                status = 'GAMES NOT OVER'

#Checks that the value in a row is equal to the next value in the column
    for i in range(4):
        for j in range(4):
            if j+1 <= 3:
                if (matriz[i][j] == matriz[i][j+1]):
                    status = 'GAMES NOT OVER'

#Checks that the value in a column is equal to the next value in the row
    for i in range(4):
        for j in range(4):
            if i+1 <= 3:
                if (matriz[i][j] == matriz[i+1][j]):
                    status = 'GAMES NOT OVER' 
    return status

#We compress the grid to swipe to the left
def compress_the_grid(matriz):
    is_changed = False
    new_matrix = [[0]*4 for _ in range(4)]
    for i in range(4):
        previus_position = 0
        for j in range(4):
            if(matriz[i][j] !=0):
                new_matrix[i][previus_position] = matriz[i][j]
                if(j!=previus_position):
                    is_changed = True
                previus_position += 1
    return new_matrix,is_changed

#Merge the values of the grid in the case they are equal
def merge_values(matriz):
    is_changed = False
    for i in range(4):
        for j in range(3):
            if matriz[i][j+1] == matriz[i][j] and matriz[i][j] != 0:
                matriz[i][j] = matriz[i][j] * 2
                matriz[i][j+1] = 0
                is_changed = True

    return matriz, is_changed
#functions to  control the matrix and return a new matrix
def reverse_matrix(matriz):
    new_matriz = [list(reversed(matriz[i])) for i in range(4)]
    return new_matriz

def tranpose_matrix(matriz):
    new_matrix = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
    return new_matrix

#Function depending the command
#For the left command
#1. Compress the grid
#2.Merge the value
#3. Compress Again
def command_left(matriz):
    new_grid, is_changed_1 = compress_the_grid(matriz)
    new_grid, is_changed_2 = merge_values(new_grid)
    is_changed = is_changed_1 or is_changed_2
    new_grid, temp = compress_the_grid(new_grid)
    return new_grid, is_changed

#For the rigth command
#1.Reverse the grid
#2. we call the command left
#3. Reverse the grid Again
def command_rigth(matriz):
    new_grid = reverse_matrix(matriz)
    new_grid,is_changed = command_left(new_grid)
    new_grid = reverse_matrix(new_grid)
    return new_grid, is_changed

#For the up command
#1. Transpose the grid
#2. we call the command left
#3. Tranpose the grid Again
def command_up(matriz):
    new_grid = tranpose_matrix(matriz)
    new_grid, is_changed = command_left(new_grid)
    new_grid = tranpose_matrix(new_grid)
    return new_grid,is_changed

#For the up command
#1. Transpose the grid
#2. we call the command rigth
#3. Tranpose the grid Again
def command_down(matriz):
    new_grid = tranpose_matrix(matriz)
    new_grid, is_changed = command_rigth(new_grid)
    new_grid = tranpose_matrix(new_grid)
    return new_grid, is_changed
