import sys
import os
import copy
sys.path.append(os.path.abspath('..\\game'))

class Tree(object):
    def __init__(self):
        self.up = None
        self.down = None
        self.layer = None
        self.state = 'Unsettled'
        self.nt = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def find_all():
    def init_obj():
        a = Tree()
        a.up = []
        a.down = []
        a.layer = 0
        return a

    def chk_pos(board, num):
        temp = num in range(1, 10)
        temp_2 = board[num - 1] not in {'O', 'X'}
        return temp and temp_2

    def find_num(board):
        A = []
        for i in range(9):
            if chk_pos(board, i + 1):
                A.append(i + 1)
        return A

    def check_board(board):
        win_combination = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        count = 0
        for a in win_combination:
            if board[a[0]] == board[a[1]] == board[a[2]] == "X":
                return 'X'

            if board[a[0]] == board[a[1]] == board[a[2]] == "O":
                return 'O'

        for a in range(9):
            if board[a] == "X" or board[a] == "O":
                count += 1
            if count == 9:
                return 'Tie'
        return 'Unsettled'

    A = []
    # 0th layer
    A.append(init_obj())
    A[0].nt = find_num(A[0].board)
    A[0].State = check_board(A[0].board)

    # 1st layer
    for i in A[0].nt:
        temp = init_obj()
        temp.layer = 1
        temp.up = 0
        temp.board[i - 1] = 'X'
        temp.nt = find_num(temp.board)
        temp.state = check_board(temp.board)
        A.append(temp)

    for i in range(len(A)):
        if i == 0:
            continue
        else:
            if A[i].up == 0:
                A[0].down.append(i)

    # 2nd layer
    for i in A[0].down:
        for j in A[i].nt:
            temp = init_obj()
            temp.layer = 2
            temp.up = i
            temp.board = copy.deepcopy(A[i].board)
            temp.board[j - 1] = 'O'
            temp.nt = find_num(temp.board)
            temp.state = check_board(temp.board)
            A.append(temp)

    for i in range(len(A)):
        if A[i].layer == 0 or A[i].layer == 1:
            continue
        else:
            if A[i].layer == 2:
                A[A[i].up].down.append(i)

    # 3rd layer
    for i in range(len)

    return  A

if __name__ == '__main__':
   a = find_all()
