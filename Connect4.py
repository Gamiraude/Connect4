import numpy as np
from enum import Enum
import random
import time

move_status = Enum('move_status', ['invalid_row', 'invalid_column', 'valid'])
grid = np.zeros((6,7))
counter = 0
status = move_status.valid

def player(counter):
    if counter % 2 == 0:
        return 1
    else:
        return 2
    
def moveRegistration(move):
    row = 5
        
    while True:
        if 0 > move - 1 or move - 1 > 6:
            return move_status.invalid_column, ()
        elif row < 0:
            return move_status.invalid_row, ()
        else:
            if grid[row, move - 1] != 0:
                row -= 1
            elif grid[row, move - 1] == 0:
                grid[row, move - 1] = player(counter)
                return move_status.valid, (player(counter), row, move - 1)     
        
def winConditionDiagonalsOrLeftRight(current_move, grid, xmodification, ymodification):
    winCounter = 1
    x = current_move[1]
    y = current_move[2]

    while winCounter < 4:
        if 0 <= x + xmodification < 6 and 0 <= y - ymodification < 7:
            if grid[x + xmodification, y - ymodification] == current_move[0]:
                winCounter += 1
                x += xmodification
                y -= ymodification
            else:
                break
        else:
            break

    x = current_move[1]
    y = current_move[2]

    while winCounter < 4:
        if 0 <= x - xmodification < 6 and 0 <= y + ymodification < 7:
            if grid[x - xmodification, y + ymodification] == current_move[0]:
                winCounter += 1
                x -= xmodification
                y += ymodification
            else:
                break
        else:
            break

    return winCounter > 3

def winCondition(current_move, grid):
    return (winConditionDiagonalsOrLeftRight(current_move, grid, 1, 1) or
            winConditionDiagonalsOrLeftRight(current_move, grid, 1, -1) or
            winConditionDiagonalsOrLeftRight(current_move, grid, 0, 1) or
            winConditionDiagonalsOrLeftRight(current_move, grid, 1, 0))

def pvp():
    global counter
    global status
    global grid

    while True:
        try:
            print('\n')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*')
            print(f'It is Player {player(counter)} turn.')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*\n')
            print(grid)
            print('\n')
            
            if status == move_status.invalid_column:
                print('The number you enter must be in between 1 and 7!')
            elif status == move_status.invalid_row:
                print(f'All spots in column {move} are taken. Please choose a different column')

            move = int(input('Choose your move (number from 1 to 7):'))

            status, current_move = moveRegistration(move)
                    
            if status == move_status.valid:                   
                if winCondition(current_move, grid):
                    print(grid)
                    print('\n')
                    print(f'Player {current_move[0]} won!')
                    print('CONGRATULATIONS! \\o/')
                    break
                counter += 1
        except ValueError:
            print('You must enter a number between 1 and 7!')
            move = int(input('Choose your move (number from 1 to 7):'))

def pve():
    pc_choice = [1,2,3,4,5,6,7]
    global counter
    global status
    global grid

    while True:
        try:
            print('\n')
            print(grid)
            print('\n')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*')
            print(f'It is Player {player(counter)} turn.')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*')
            
            if status == move_status.invalid_column:
                print('The number you enter must be in between 1 and 7!')
            elif status == move_status.invalid_row:
                print(f'All spots in column {move} are taken. Please choose a different column')

            if player(counter) == 1:
                move = int(input('\nChoose your move (number from 1 to 7): '))
            elif player(counter) == 2:
                move = random.choice(pc_choice)
                time.sleep(1)

            status, current_move = moveRegistration(move)
                    
            if status == move_status.valid:                  
                if winCondition(current_move, grid):
                    print(grid)
                    print('\n')
                    print(f'Player {current_move[0]} won!')
                    print('CONGRATULATIONS! \\o/')
                    break
                counter += 1
        except ValueError:
            print('You must enter a number between 1 and 7!')
            move = int(input('Choose your move (number from 1 to 7):'))



print('*-*-*-*-*-*-*-*-*-*-*-*-*')
print('Welcome to the Connect 4!')
print('*-*-*-*-*-*-*-*-*-*-*-*-*\n')

while True:
        choice = str(input('Would you like to play against another player or computer (p/c)?')).lower()
        if choice == 'p':
            pvp()
            break
        elif choice == 'c':
            pve()
            break   
        else:
            print('Your choice must be p or c!')