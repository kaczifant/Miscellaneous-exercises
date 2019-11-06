# 3x3 tic-tac-toe game implemented on my own from sratch

def draw_table():
    
    for i in range(len(table)):
        for j in range(len(table[i])):
            if str(table[i][j]).isdigit():
                print('.', end= ' ')
            else:
                print(table[i][j], end= ' ')
        print()
    return

def check_winner():
    
    diagonal_left = set()
    diagonal_right = set()
    k = len(table[0]) - 1

    for i in range(len(table)):
        row = set()
        col = set()

        diagonal_left.add(table[i][i])
        diagonal_right.add(table[i][k])
        k -= 1

        for j in range(len(table[i])):
            row.add(table[i][j])
            col.add(table[j][i])
        if len(row) == 1 or len(col) == 1:
            return True

    if len(diagonal_left) == 1 or len(diagonal_right) == 1:
        return  True
    return False
    

def check_and_update(step, player):

    if not step.isdigit() or int(step) < 1 or int(step) > 9:
        print("Invalid step, try again!")
        return -1
    
    index = int(step) - 1
    # Defining row
    i = index // 3
    # Defining column
    j = index % 3

    if table[i][j] == 'X' or table[i][j] == 'O':
        print("Position already occupied, try again!")
        return -1
    else:
        if player == 1:
            table[i][j] = 'X'
            return 0
        else:
            table[i][j] = 'O'
            return 0


if __name__ == "__main__":
    
    # Draw initial table with positions
    table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    for i in range(len(table)):
        for j in range(len(table[i])):
            print(table[i][j], end= ' ')
        print()
    
    draw_table()
    
    # Player 1: X
    # Player 2: O
    
    won = False
    step_counter = 0
    
    print("Enter where you want to put X or O")
    
    while step_counter < 9:
    
        return_value_1 = -1
        
        while return_value_1 == -1:
            player_1_step = input("Player 1 (X): ")
            print()
            return_value_1 = check_and_update(player_1_step, 1)
            if return_value_1 == 0:
                step_counter += 1
        draw_table()
    
        won = check_winner()
        if won:
            print("Player 1 won. Congratulations!")
            break
        if step_counter == 9:
            print("The table is full. END of GAME.")
            break
       

        return_value_2 = -1

        while return_value_2 == -1:
            player_2_step = input("Player 2 (O): ")
            print()
            return_value_2 = check_and_update(player_2_step, 2)
            if return_value_2 == 0:
                step_counter += 1
        draw_table()
       
        won = check_winner()
        if won:
            print("Player 2 won. Congratulations!")
            break
        if step_counter == 9:
            print("The table is full. END of GAME.")
            break

   
    