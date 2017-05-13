import random




def drawBoard(matrix):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + str(matrix[2][0]) + ' | ' + str(matrix[2][1]) + ' | ' + str(matrix[2][2]))
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + str(matrix[1][0]) + ' | ' + str(matrix[1][1]) + ' | ' + str(matrix[1][2]))
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + str(matrix[0][0]) + ' | ' + str(matrix[0][1]) + ' | ' + str(matrix[0][2]))
    print('   |   |')
        
def check_tic_tac_toe_game(matrix,player1_name,player2_name):
    global player1_score 
    global player2_score 
    
    winner = ''
    #horizontal checking  
    for i in range(0,3):
        
        if matrix[i][0] == matrix[i][1]== matrix[i][2] =='x':
            winner = player1_name
            player1_score = player1_score + 1
            print("%s is winner" %player1_name)
    
        elif matrix[i][0] == matrix[i][1]== matrix[i][2] =='o':
            winner = player2_name
            player2_score = player2_score + 1
            print("%s is winner" %player2_name)
        
         
    #vertical checking
    for j in range(0,3):
        if matrix[0][j] == matrix[1][j]== matrix[2][j] =='x':
            winner = player1_name
            player1_score = player1_score + 1
            print("%s is winner" %player1_name)
    
        elif matrix[0][j] == matrix[1][j]== matrix[2][j] =='o':
            winner = player2_name
            player2_score = player2_score + 1
            print("%s is winner" %player2_name)
        
        
    # diagonal checking
    if matrix[0][0] == matrix[1][1] == matrix[2][2] == 'x':
        winner = player1_name
        player1_score = player1_score + 1
        print("%s is winner" %player1_name)
    
    elif matrix[0][0] == matrix[1][1] == matrix[2][2] == 'o':
        winner = player2_name
        player2_score = player2_score + 1
        print("%s is winner" %player2_name)
        
    elif matrix[2][0] == matrix[1][1] == matrix[0][2] == 'x':
        winner = player1_name
        player1_score = player1_score + 1
        print("%s is winner" %player1_name)
        
    elif matrix[2][0] == matrix[1][1] == matrix[0][2] == 'o':
        winner = player2_name
        player2_score = player2_score + 1
        print("%s is winner" %player2_name)
        
    # check else condition for game is tie       
    # return who is the winner or tie    
    if winner != player1_name and winner != player2_name:
        winner = 'tie'
   
   
    return winner,player1_score,player2_score


def check_game_winner(winner,player1_name, player2_name):
    
    print("Checking the winner")     
    if winner == player1_name:
        print("Congratulations! %s" %player1_name) 
        
        return "success"
    elif winner == player2_name:
        print("Congratulations! %s" %player2_name) 
        
        return "success"
    else:
        return "try-again"

def check_board_is_full(matrix):
    
    print("Checking the board is full")
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j])
            if matrix[i][j] != 0:
                continue
            else:
                return "not-full"
    return "success"
    
def choose_first(player1_name,player2_name):
    first_player = random.randint(1,2)
    
    if first_player == 1:
        return player1_name 
    else:
        return player2_name
    
    if first_player == 2:
        return player2_name 
    else:
        return player1_name
    
    
def error_checking(value):
   
    print("Inside error checking")
    
    if value[0].isdigit():
        print("inside if loop")
        status = "success"
    else:
        print("inside else")
        status ="failure"
        
    
    if value[1].isdigit():
        print("inside if loop")
        status1 = "success"
        
    else:
        print("inside else")
        status1 ="failure1"
        
    if len(value) == 2:
        print("Inside length check")
        status2 = "success"
    else:
        status2 = "failure2"
    
        
    return status,status1,status2
   
def process_player_input(player_input,player_symbol,player1_name,player2_name,first_player, matrix):
    if "," not in player_input: 
        print(" comma not in the input, Enter valid format") 
        return "comma-failure"
    value = player_input.split(",")
    status,status1,status2 = error_checking(value)
    if status2 == "failure2":
        return "failure" 
    if status == "success" and status1 == "success" and status2 == "success":
        row = int(value[0])
        col = int(value[1])
        if col <= 2 and row <= 2: 
            print("starting to store inputs")
        
            if matrix[row][col] != 'x' and matrix[row][col] !='o':
                if first_player == player1_name:
                    matrix[row][col] = player_symbol
                    print(matrix[row][col])
                   
                elif first_player == player2_name:
                    matrix[row][col] = player_symbol
                    print(matrix[row][col])
                    
                else:
                    pass
        
                return "success"
            else:
                return "try-again"
        else:
            print("number error")
            return "number-error"
        
    else:
        print("inside else loop")
        return "failure"


print("Welcome to Tic Tac Toe!")

while True:
    player1_name = input("Player 1 enter your name:")
    if player1_name == "":
        continue
    else:
        break
    

while True:
    player1_symbol = input("Choose either x or o as your symbol:")
    if player1_symbol == 'x' or player1_symbol == 'o':
        break
    else:
        print("Enter the correct player symbol")
        continue
        
while True:
    player2_name = input("Player 2 enter your name:")
    if player2_name == "":
        continue
    else:
        break

first_player = choose_first(player1_name,player2_name)
print(first_player)
player1_score = 0
player2_score = 0

while True:
    matrix = [[0 for i in range(3)] for j in range(3)] 
    count_player1 = 0
    count_player2 = 0
   
    
    while True:
    
        if first_player == player1_name:
            
            drawBoard(matrix)
            
            print(first_player)
            player_input = input("Enter the row, column you want to put %s:" %player1_symbol)
            
            if player_input == 'q':
                break
            
            result = process_player_input(player_input,player1_symbol,player1_name,player2_name,first_player,matrix)
            print(result)
            if result == "success":
                count_player1 = count_player1 + 1
                print(count_player1) 
            if result == "try-again":
                print("Enter different row and column The row and column are filled")
                continue
            if result == "failure":
                print("Please enter digits")
                continue
            if result == "number-error":
                print("please enter number from 0 to 2 in the format 0,0")
                continue
            if result == "comma-failure":
                print("Please enter in the following format 0,0 ")
                continue
    
            winner,player1_score,player2_score = check_tic_tac_toe_game(matrix,player1_name,player2_name)
            result1 = check_game_winner(winner,player1_name,player2_name)
            drawBoard(matrix)
            if result1 == "success":
                break
            first_player = player2_name
            
        else:
            drawBoard(matrix) 
            print("%s" %player2_name) 
            if player1_symbol == 'x':
                player2_symbol = 'o'
            elif player1_symbol == 'o':
                player2_symbol = 'x'
            else:
                pass
                
            player_input = input("Enter the row, column you want to put %s:" %player2_symbol)  
            if player_input == 'q':
                break 
    
            result = process_player_input(player_input,player2_symbol,player1_name,player2_name,first_player,matrix)
            print(result)
            if result == "success":
                count_player2 = count_player2 + 1
                print(count_player2) 
            if result == "try-again":
                print("Enter different row and column The row and column are filled")
                continue
            if result == "failure":
                print("Please enter digits")
                continue
            if result == "number-error":
                print("please enter number from 0 to 2 in the format 0,0")
                continue
            if result == "comma-failure":
                print("Please enter in the following format 0,0 ")
                continue
    
            winner,player1_score,player2_score = check_tic_tac_toe_game(matrix,player1_name,player2_name)
            result1 = check_game_winner(winner,player1_name,player2_name)
            drawBoard(matrix)
            if result1 == "success":
                break
            first_player = player1_name
    
        # Checking for game tie
        result = check_board_is_full(matrix)
        print(result)
        if result == "success":
            print("Checking game for tie")
            winner,player1_score,player2_score = check_tic_tac_toe_game(matrix,player1_name,player2_name) 
            print(winner)
            print(player1_score)
            print(player2_score)
            if winner == 'tie' and player1_score == 0 and player2_score == 0:
                drawBoard(matrix)
                print("Game is tie")
                break
          
          
    next_game = input('Do you want to play another game, type Yes/No to play:')  
    print(next_game)
    if next_game == 'Yes' or next_game == 'yes':
        continue
    elif next_game == 'No' or next_game == 'no':
        
        print("%s score is %d" %(player1_name,player1_score))
        print("%s score is %d" %(player2_name,player2_score))
        
        if player1_score == player2_score:
            print("tie")     
        elif player1_score > player2_score:
            print("%s is the winner" %player1_name)
        else:
            print("%s is the winner" %player2_name)
        break





