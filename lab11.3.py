#!/usr/bin/python
#-*- coding: utf-8 -*-
board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
marks = ['x','o']
computer = []
player = []

wins = [[0,1,2], [3,4,5], [6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]


def isWinner(bo, le):
    return ((bo[0] == le and bo[1] == le and bo[2] == le) or  # across the top
            (bo[3] == le and bo[4] == le and bo[5] == le) or  # across the middle
            (bo[6] == le and bo[7] == le and bo[8] == le) or  # across the bottom
            (bo[0] == le and bo[3] == le and bo[6] == le) or  # down the left side
            (bo[1] == le and bo[4] == le and bo[7] == le) or  # down the middle
            (bo[2] == le and bo[5] == le and bo[8] == le) or  # down the right side
            (bo[0] == le and bo[4] == le and bo[8] == le) or  # diagonal
            (bo[2] == le and bo[4] == le and bo[6] == le))  # diagonal


def freeCells(bo):
    count = 0
    for i in board:
        if i not in marks:
            count += 1
    return count


def takeEdge(bo,le):
    if bo[0] not in marks:
        bo[0] = le
        return 0
    elif bo[2] not in marks:
        bo[2] = le
        return 2
    elif bo[6] not in marks:
        bo[6] = le
        return 6
    elif bo[8] not in marks:
        bo[8] = le
        return 8
    else:
        return -1


def takeFree(bo,le):
    for i in bo:
        if str(i).isdigit():
            bo[i] = le
            return i


def computer_move(bo, le):
    if bo[4] == 4:
        bo[4] = le
        computer.append(4)
        return
    if freeCells(bo) >= 7:
        computer.append(takeEdge(bo, le))
        return
    if marks[0] == le:
        enemy = marks[1]
    else:
        enemy = marks[0]

    for win in wins:
        if len(set(win) & set(computer)) == 2:
            i = (set(win) - set(computer)).pop()
            if bo[i] not in marks:
                bo[i] = le
                computer.append(i)
                return

    for win in wins:
        if len(set(win) & set(player)) == 2:
            i = (set(win) - set(player)).pop()
            if bo[i] not in marks:
                bo[i] = le
                computer.append(i)
                return

    edge = takeEdge(bo, le)
    if edge != -1:
        computer.append(edge)
        return

    computer.append(takeFree(bo, le))


def getUserMove(bo):
    try:
        move = int(input("Enter cell number "))
        if bo[move] in marks:
            return getUserMove(bo)
        else:
            return move
    except:
        return getUserMove(bo)


def getFigure():
    figure = input("Choose x or o ")
    if figure in marks:
        return figure
    else:
        return getFigure()


def printBoard(bo):
    print("{} {} {}\n{} {} {}\n{} {} {}".format(board[0],board[1],board[2],board[3],board[4],board[5],board[6],
                                                board[7],board[8]))


def startGame(bo):
    user = getFigure()
    if marks[0] == user:
        computerFigure = marks[1]
    else:
        computerFigure = marks[0]

    if computerFigure == 'x':
        computer_move(bo, computerFigure)

    for i in range(5):
        printBoard(bo)
        move = getUserMove(bo)
        player.append(move)
        bo[move]=user
        if isWinner(bo, user):
            print("You won!")
            return
        printBoard(bo)
        computer_move(bo, computerFigure)
        if isWinner(bo, computerFigure):
            print("Computer won!")
            printBoard(bo)
            return


startGame(board)