import random 
def add_new_2(matriz):
    random_row = random.randint(0,3)
    random_column = random.randint(0,3)

    while matriz[random_row][random_column] !=0:
        print("estoy en el loop")
        random_row = random.randint(0,3)
        random_column = random.randint(0,3)

    matriz[random_row][random_column] = 2

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

def get_current_state(matriz):
    status = "YOU LOST"

    for i in range(4):
        for j in range(4):
            if matriz[i][j] == 2048:
                status = 'YOU WON'

    for i in range(4):
        for j in range(4):
            if matriz[i][j] == 0:
                status = 'GAMES NOT OVER'

    for i in range(4):
        for j in range(4):
            if j+1 <= 3:
                if (matriz[i][j] == matriz[i][j+1]):
                    status = 'GAMES NOT OVER'
    for i in range(4):
        for j in range(4):
            if i+1 <= 3:
                if (matriz[i][j] == matriz[i+1][j]):
                    status = 'GAMES NOT OVER' 
    return status

def command_up(matriz):
    print("comando arriba")

def command_down(matriz):
    print("comando abajo")

def command_left(matriz):
    print("comando izquierda")

def command_rigth(matriz):
    print("comando derecha")