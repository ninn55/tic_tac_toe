from msvcrt import getch
import os
from Draw import draw
from colorama import init, Fore

init()

def play_1():
    init_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        if i == 0:
            os.system('clear')
            board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            print("Let's play Tic_Tac_Toe")
            print("press number to play")
            draw(init_board)
            draw(board)
        temp = user_input(board) - 1
        os.system('clear')
        print("Let's play Tic_Tac_Toe")
        print("press number to play")
        draw(init_board)
        if i % 2 == 0:
            board = update_board(board, temp, 'X')
            draw(board)
            if check_board(board):
                break
        else:
            board = update_board(board, temp, 'O')
            draw(board)
            if check_board(board):
                break
    return 0

def user_input(board):
    #tested
    while True:
        temp = read_key()
        try:
            temp = int(temp)
        except:
            print('invalid input')
        else:
            if temp in range(1, 10):
                if board[temp - 1] in {'O', 'X'}:
                    print('try another location')
                    continue
                else:
                    return temp
            else:
                print('invalid input')
                continue
        
def read_key():
    return getch().decode('UTF-8')

def update_board(board, op, piece):
    if len(board) != 9:
        print('\n')
        print('A error has accrue, use ctrl + c to interupt the program')
    else:
        if piece in ['X', 'O']:
            if op in range(9):
                if board[op] not in ['X', 'O']:
                    board[op] = piece
                else:
                    print('\n')
                    print('please input again')
                    return board
            else:
                print('\n')
                print('A error has accrue, use ctrl + c to interupt the program')

        else:
            print('\n')
            print('A error has accrue, use ctrl + c to interupt the program')
    return board

def check_board(board):
    win_commbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    count = 0
    for a in win_commbinations:
        if board[a[0]] == board[a[1]] == board[a[2]] == "X":
            print(Fore.GREEN + "Player 1 Wins!")
            print(Fore.GREEN + "Congratulations!")
            return True

        if board[a[0]] == board[a[1]] == board[a[2]] == "O":
            print(Fore.RED + "Player 2 Wins!")
            print(Fore.RED + "Congratulations!")
            return True
    for a in range(9):
        if board[a] == "X" or board[a] == "O":
            count += 1
        if count == 9:
            print("The game ends in a Tie\n")
            return True

def check_board_2(board):
    win_commbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    count = 0
    for a in win_commbinations:
        if board[a[0]] == board[a[1]] == board[a[2]] == "X":
            return 1

        if board[a[0]] == board[a[1]] == board[a[2]] == "O":
            return 2

    for a in range(9):
        if board[a] == "X" or board[a] == "O":
            count += 1
        if count == 9:
            return 3
    
    return 0

if __name__ == '__main__':
    #board = [7, 8, 9, 4, 5, 6, 1, 2, 3]
    #board = ['X', 'O', 'O', 4, 5, 6, 1, 2, 3]
    #print(update_board(board, 1, 'X') == board)
    #print(user_input(['X', 'O', 'O', 4, 5, 6, 1, 2, 3]))
    #print(check_board_2(['X', 'O', 'O', 4, 5, 6, 1, 2, 3]))
    play_1()