import logic

if __name__ == "__main__":
    matriz = logic.start_game()
    for i in range(4):
        print(matriz[i])
    while True:
        print("Choose an option:")
        command = input(">>").upper()
        match command:
            case 'W':
                print("UP")
                matriz, flag = logic.command_up(matriz)
                status = logic.get_current_state(matriz)
                if status=="GAMES NOT OVER":
                    logic.add_new_2(matriz)
                for i in range(4):
                    print(matriz[i])
            case 'S':
                print("DOWN")
                matriz, flag = logic.command_down(matriz)
                status = logic.get_current_state(matriz)
                if status=="GAMES NOT OVER":
                    logic.add_new_2(matriz)
                for i in range(4):
                    print(matriz[i])
            case 'A':
                print("LEFT")
                matriz, flag = logic.command_left(matriz)
                status = logic.get_current_state(matriz)
                if status=="GAMES NOT OVER":
                    logic.add_new_2(matriz)
                for i in range(4):
                    print(matriz[i])
            case 'D':
                print("RIGHT")
                matriz, flag = logic.command_rigth(matriz)
                status = logic.get_current_state(matriz)
                if status=="GAMES NOT OVER":
                    logic.add_new_2(matriz)
                for i in range(4):
                    print(matriz[i])
            case _:
                print("Invalid command")
    
