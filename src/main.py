import logic

if __name__ == "__main__":
    matriz = logic.start_game()
    print(matriz)
    while True:
        print("Please introduce your command:")
        command = input(">>").upper()
        match command:
            case 'W':
                print("Up")
                status = logic.get_current_state(matriz)
                print(status)
                logic.command_up(matriz)
            case 'S':
                print("Down")
                status = logic.get_current_state(matriz)
                print(status)
                logic.command_down(matriz)
            case 'A':
                print("Left")
                status = logic.get_current_state(matriz)
                print(status)
                logic.command_left(matriz)
            case 'D':
                print("Rigth")
                status = logic.get_current_state(matriz)
                print(status)
                logic.command_rigth(matriz)
            case _:
                print("Introduce a valid command")
            
    
