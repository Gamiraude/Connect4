import numpy as np

def player(counter):
    if counter % 2 == 0:
        return 1
    else:
        return 2
    
def moveRegistration(move):
    row = 5
        
    while True:
        if 0 <= move - 1 < 7 and 0 <= row:
            if grid[row, move - 1] != 0:
                row -= 1
            elif grid[row, move - 1] == 0:
                grid[row, move - 1] = player(counter)
                return (player(counter), row, move - 1)
        else:
            row = 5
            print(f'All spots in column {move} are taken. Please choose a different column')
            move = int(input('Choose your move (number from 1 to 7):'))

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

print('*-*-*-*-*-*-*-*-*-*-*-*-*')
print('Welcome to the Connect 4!')
print('*-*-*-*-*-*-*-*-*-*-*-*-*\n')

grid = np.zeros((6,7))
counter = 0
    
while True:
    try:
        print('*-*-*-*-*-*-*-*-*-*-*-*-*')
        print(f'It is Player {player(counter)} turn.')
        print('*-*-*-*-*-*-*-*-*-*-*-*-*\n')
        print(grid)
        print('\n')
        
        move = int(input('Choose your move (number from 1 to 7):\n'))
        while 1 > move >= 8:            #while move not in range(1,8):
            move = int(input('The number you enter must be in between 1 and 7! Choose your move:'))
        if 1 <= move < 8:
            current_move = moveRegistration(move)
            print(grid)
            print('\n')
            if winCondition(current_move, grid):
                print(f'Player {current_move[0]} won!')
                break
            counter += 1
    except ValueError:
        print('You must enter a number between 1 and 7!')
        move = int(input('Choose your move (number from 1 to 7):'))