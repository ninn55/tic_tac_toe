# This is a early version of Enumerat.py

import sys
import os
import copy
import time
import json
import pandas as pd
sys.path.append(os.path.abspath('..\\game'))


class Tree(object):
    def __init__(self):
        self.up = None  # tree structure
        self.down = None  # tree structure
        self.layer = None  # current layer number
        self.state = 'Unsettled'
        self.nt = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # next possible move
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # current board
        self.score_1 = 0.0
        self.score_2 = 0.0


def final_chk(board):
    print(len(board))
    a = 0
    for i in range(len(board)):
        if board[i].layer == 9:
            if board[i].state == 'Unsettled':
                a += 1
                print('error')
    print(a)


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
        win_combination = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                           (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
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
    for i in range(len(A)):
        if A[i].layer == 1:
            for j in A[i].down:
                for k in A[j].nt:
                    temp = init_obj()
                    temp.layer = 3
                    temp.up = j
                    temp.board = copy.deepcopy(A[j].board)
                    temp.board[k - 1] = 'X'
                    temp.nt = find_num(temp.board)
                    temp.state = check_board(temp.board)
                    A.append(temp)

    for i in range(len(A)):
        if A[i].layer == 3:
            A[A[i].up].down.append(i)

    # 4th layer
    for i in range(len(A)):
        if A[i].layer == 2:
            for j in A[i].down:
                for k in A[j].nt:
                    temp = init_obj()
                    temp.layer = 4
                    temp.up = j
                    temp.board = copy.deepcopy(A[j].board)
                    temp.board[k - 1] = 'O'
                    temp.nt = find_num(temp.board)
                    temp.state = check_board(temp.board)
                    A.append(temp)

    for i in range(len(A)):
        if A[i].layer == 4:
            A[A[i].up].down.append(i)

    # 5th layer
    for i in range(len(A)):
        if A[i].layer == 3:
            for j in A[i].down:
                for k in A[j].nt:
                    temp = init_obj()
                    temp.layer = 5
                    temp.up = j
                    temp.board = copy.deepcopy(A[j].board)
                    temp.board[k - 1] = 'X'
                    temp.nt = find_num(temp.board)
                    temp.state = check_board(temp.board)
                    if temp.state != 'Unsettled':
                        temp.nt = []
                    A.append(temp)

    for i in range(len(A)):
        if A[i].layer == 5:
            A[A[i].up].down.append(i)

    # 6th layer
    for i in range(len(A)):
        if A[i].layer == 4:
            for j in A[i].down:
                for k in A[j].nt:
                    temp = init_obj()
                    temp.layer = 6
                    temp.up = j
                    temp.board = copy.deepcopy(A[j].board)
                    temp.board[k - 1] = 'O'
                    temp.nt = find_num(temp.board)
                    temp.state = check_board(temp.board)
                    if temp.state != 'Unsettled':
                        temp.nt = []
                    A.append(temp)

    for i in range(len(A)):
        if A[i].layer == 6:
            A[A[i].up].down.append(i)

    # 7th layer
    for i in range(len(A)):
        if A[i].layer == 5:
            for j in A[i].down:
                for k in A[j].nt:
                    temp = init_obj()
                    temp.layer = 7
                    temp.up = j
                    temp.board = copy.deepcopy(A[j].board)
                    temp.board[k - 1] = 'X'
                    temp.nt = find_num(temp.board)
                    temp.state = check_board(temp.board)
                    if temp.state != 'Unsettled':
                        temp.nt = []
                    A.append(temp)

    for i in range(len(A)):
        if A[i].layer == 7:
            A[A[i].up].down.append(i)

    # 8th layer
    for i in range(len(A)):
        if A[i].layer == 6:
            for j in A[i].down:
                for k in A[j].nt:
                    temp = init_obj()
                    temp.layer = 8
                    temp.up = j
                    temp.board = copy.deepcopy(A[j].board)
                    temp.board[k - 1] = 'O'
                    temp.nt = find_num(temp.board)
                    temp.state = check_board(temp.board)
                    if temp.state != 'Unsettled':
                        temp.nt = []
                    A.append(temp)

    for i in range(len(A)):
        if A[i].layer == 8:
            A[A[i].up].down.append(i)

    # 9th layer
    for i in range(len(A)):
        if A[i].layer == 7:
            for j in A[i].down:
                for k in A[j].nt:
                    temp = init_obj()
                    temp.layer = 9
                    temp.up = j
                    temp.board = copy.deepcopy(A[j].board)
                    temp.board[k - 1] = 'X'
                    temp.nt = find_num(temp.board)
                    temp.state = check_board(temp.board)
                    if temp.state != 'Unsettled':
                        temp.nt = []
                    A.append(temp)

    for i in range(len(A)):
        if A[i].layer == 9:
            A[A[i].up].down.append(i)

    return A


def score(A):
    for i in range(len(A)):
        if A[i].layer == 9:
            if A[i].state == 'X':
                A[i].score_1 = 1
            elif A[i].state == 'O':
                A[i].score_2 = 1
            else:
                pass

    for k in [8, 7, 6, 5, 4, 3, 2, 1, 0]:
        for i in range(len(A)):
            if A[i].layer == k:
                if A[i].state == 'X':
                    A[i].score_1 = 1
                elif A[i].state == 'O':
                    A[i].score_2 = 1
                else:
                    temp_1 = 0
                    temp_2 = 0
                    for j in A[i].down:
                        temp_1 = temp_1 + A[j].score_1
                        temp_2 = temp_2 + A[j].score_2
                    A[i].score_1 = temp_1 / len(A[i].down)
                    A[i].score_2 = temp_2 / len(A[i].down)

    return A


def to_json(A):
    O = {}
    for i in range(len(A)):
        O[i] = {
            'up': A[i].up,
            'down': A[i].down,
            'layer': A[i].layer,
            'state': A[i].state,
            'nt': A[i].nt,
            'board': A[i].board,
            'score_1': A[i].score_1,
            'score_2': A[i].score_2}
    with open('assets//data.json', 'w') as outfile:
        json.dump(O, outfile)


def to_df(A):
    O = {
        'up': [
            0 for i in range(
                len(A))], 'down': [
            0 for i in range(
                len(A))], 'layer': [
            0 for i in range(
                len(A))], 'state': [
            0 for i in range(
                len(A))], 'nt': [
            0 for i in range(
                len(A))], 'board': [
            0 for i in range(
                len(A))], 'score_1': [
            0 for i in range(
                len(A))], 'score_2': [
            0 for i in range(
                len(A))]}
    for i in range(len(A)):
        O['up'][i] = A[i].up
        O['down'][i] = A[i].down
        O['layer'][i] = A[i].layer
        O['state'][i] = A[i].state
        O['nt'][i] = A[i].nt
        O['board'][i] = A[i].board
        O['score_1'][i] = A[i].score_1
        O['score_2'][i] = A[i].score_2
    P = pd.DataFrame(data=O)
    pd.DataFrame.to_csv(P, 'assets//data.csv', encoding='utf-8')


if __name__ == '__main__':
    startTime = time.time()
    b = find_all()
    final_chk(b)
    b = score(b)
    # to_json(a)
    to_df(a)
    print('The script took {0} second !'.format(time.time() - startTime))
