# python code for tic tac toe game 
import random

players = []

def even(num):
    if num % 2 == 0:
        return True
    else:
        return False

def player_details():  # this will contain names of both player
    name = input("enter the name of player: ")
    players.append(name)
    name = input("enter the name of player: ")
    players.append(name)
print('welcome to the game of tic tac toe')
player_details()
random.shuffle(players)
global player1
global player2
player1 = players[0]  # X for player1
player2 = players[1]  # O for player2


elements_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def display_board(elements=elements_list):
    board = f'''
                  |       |
              {elements_list[6]}   |   {elements_list[7]}   |   {elements_list[8]}
                  |       |
             -----------------------
                  |       |
              {elements_list[3]}   |   {elements_list[4]}   |   {elements_list[5]}
                  |       |
            ------------------------
                  |       |
              {elements_list[0]}   |   {elements_list[1]}   |   {elements_list[2]}
                  |       |

                                                                                 '''
    print(board)

def space_check(position):
    if (elements_list[position - 1] == 'X' or elements_list[position - 1] == 'O'):
        return False
    else:
        return True

def player_input(turn=player1):
    if (turn == player1):
        register = int(input("for player 1 enter the position: "))
        if (space_check(register)):
            elements_list[register - 1] = 'X'
    else:
        register = int(input('for player 2 enter the position: '))
        if space_check(register):
            elements_list[register - 1] = 'O'

def full_board_check():
    board_full = False
    for i in range(1, 10):
        if (not(space_check(i))):
            pass
        else:
            break
    else:
        board_full = True
        print('board is full match draw')
    return board_full

def win_check():
    case1 = elements_list[0] == 'X' and elements_list[1] == 'X' and elements_list[2] == 'X'
    case2 = elements_list[3] == 'X' and elements_list[4] == 'X' and elements_list[5] == 'X'
    case3 = elements_list[6] == 'X' and elements_list[7] == 'X' and elements_list[8] == 'X'
    case4 = elements_list[0] == 'X' and elements_list[4] == 'X' and elements_list[8] == 'X'
    case5 = elements_list[2] == 'X' and elements_list[4] == 'X' and elements_list[6] == 'X'

    case6 = elements_list[0] == 'O' and elements_list[1] == 'O' and elements_list[2] == 'O'
    case7 = elements_list[3] == 'O' and elements_list[4] == 'O' and elements_list[5] == 'O'
    case8 = elements_list[6] == 'O' and elements_list[7] == 'O' and elements_list[8] == 'O'
    case9 = elements_list[0] == 'O' and elements_list[4] == 'O' and elements_list[8] == 'O'
    case10 = elements_list[2] == 'O' and elements_list[4] == 'O' and elements_list[6] == 'O'

    if (case1 or case2 or case3 or case4 or case5):
        print('player 1 ', player1, 'is the winner')
        return True
    elif(case6 or case7 or case8 or case9 or case10):
        print('player 2 ', player2, 'is the winner ')
        return True
    else:
        return False

temperory = 1

'''print('welcome to the game of tic tac toe')
player_details()
random.shuffle(players)
player1 = players[0]  # X for player1
player2 = players[1]  # O for player2'''
print('player 1 is ', players[0])
print('player 2 is ', players[1])
display_board()

while not(full_board_check()) and not(win_check()):
    if even(temperory):
        player_input(turn=player1)
        display_board()
    else:
        player_input(turn=player2)
        display_board()
    temperory+=1

    if win_check():
        break
