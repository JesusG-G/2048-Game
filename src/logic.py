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


#Function depending the command
def command_up(matriz):
    print("comando arriba")

def command_down(matriz):
    print("comando abajo")

def command_left(matriz):
    print("comando izquierda")

def command_rigth(matriz):
    print("comando derecha")