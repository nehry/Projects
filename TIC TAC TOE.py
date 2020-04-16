#Global Variables
testboard = ([' '])*10
board = ([' ',' ',' ',' ',' ',' ',' ',' ',' ',])
game_state = True
turn_state = True
def display_board(board):
    #Function for designing the board
    print ('   |   |   ')
    print ('{}  | {} | {} '.format(board[6],board[7],board[8])) #This is where the X and O will go
    print ("   |   |   ")
    print ("-----------")
    print ("   |   |   ")
    print ('{}  | {} | {} '.format(board[3],board[4],board[5])) #This is where the X and O will go
    print ("   |   |   ")
    print ("-----------")
    print ("   |   |   ")
    print ('{}  | {} | {} '.format(board[0],board[1],board[2])) #This is where the X and O will go
    print ("   |   |   ")

    pass

def player_input():
    #Function for assigning the player whether they will be X or O
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("Player 1, Please choose whether you want X or O: ")
    player1 = marker

    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"

    return (player1,player2)


def place_marker(board, marker, board_position):
    #This function will grab the user's position
    player1, player2 = player_input()
    print ("The positions on the Tic Tac Toe will be similar to that of the Numpad. ")
    print ("Player 1 will go first as {}! ".format(player1))
    turn_state = player1
    gameisplaying = True
    count = 0
    while gameisplaying == True:
        if turn_state == player1:
            board_position = input("Player 1, please enter a number between 1 - 9 to place your {} in the corresponding position. ".format(player1))
            while int(board_position) >= 10 or int(board_position) <= 0:
                board_position = input("I'm Sorry, please enter a number between 1 - 9 to place your {} in the corresponding position. ".format(player1))
                continue
            else:
                marker = player1
                board[int(board_position) - 1] = marker
                turn_state = player2
                count = count + 1
                print (display_board(board))
                continue

        else:
            if turn_state == player2:
                board_position = input("Player 2, please enter a number between 1 - 9 to place your {} in the corresponding position. ".format(player2))
                while int(board_position) >= 10 or int(board_position) <= 0:
                    board_position = input("I'm Sorry, please enter a number between 1 - 9 to place your {} in the corresponding position. ".format(player2))
                    continue
                marker = player2
                board[int(board_position) - 1] = marker
                turn_state = player1
                count = count + 1
                print(display_board(board))
                continue

def win_horizontal():
    #Check if there's a win on the horizontal axis
    if count >= 5:
        if board[0] == board[1] == board[2]:
            return True
        elif board[3] == board[4] == board[5]:
            return True
        elif board[6] == board[7] == board[8]:
            return True
        else:
            return False

def win_vertical():
    # Check if there's a win on the vertical axis
    if count >= 5:
        if board[0] == board[3] == board[6]:
            return True
        elif board[1] == board[4] == board[7]:
            return True
        elif board[2] == board[5] == board[8]:
            return True
        else:
            return False

def win_diagonal():
    # Check if there's a win on the diagonal axis
    if count >= 5:
        if board[0] == board[4] == board[8]:
            return True
        elif board[2] == board[4] == board[6]:
            return True
        else:
            return False

def tie():
    if count == 10:
        if win_vertical() == False and win_horizontal() == False and win_diagonal() == False:
            gameisplaying = False

def scan_position(board):
    for i in board:
        while i == "X" or 1 == "O":
            print ("Sorry, that spot is already taken, please try another empty spot: ")
            continue

def play_again():
    if game_state == False:
        while retry_game != "Y" or retry_game != "N":
            retry_game = input("Do you want to play again? Y/N ")
            if retry_game == "Y":
                game()
                pass
            if retry_game == "N":
                break



display_board(testboard)
place_marker(board, "O", 2)


