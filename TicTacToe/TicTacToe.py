BOARD_SIZE_DEFAULT=3


matx=[['_','_','_'],['_','_','_'],['_','_','_']]

def printBoardLine(boardSize='', row=''):
    if row:
        print(f' {matx[row-1][0]} | {matx[row-1][1]} | {matx[row-1][2]}')
    else:
        print((('-' *boardSize + '+')*boardSize).rstrip('+'))


def printBoard():
    print('')
    for i in range(1,4):
        printBoardLine(3)
        printBoardLine(3,i)
    printBoardLine(3)
    print('')


def getPlayerInput(player):
    print(f"Player {player}, it's your turn to play!")
    cellX, cellY = input("Choose a free cell: ")
    cellX = int(cellX)
    cellY = int(cellY)
    
    return [cellX, cellY]


def validatePlayerInput(inputData):
    # sourcery skip: hoist-statement-from-if, remove-unnecessary-else
    if (1 <= inputData[0] <= 3) & (1 <= inputData[1] <= 3):
        if matx[inputData[0]-1][inputData[1]-1] == '_':
            return True
        else:
            print("No cheating - cell is already taken!")
            return False
    else:
        print("Wrong cell index chosen - please enter a free cell 1-3")
        return False


def matxUpdate(inputData, player):
    matx[inputData[0]-1][inputData[1]-1] = 'X' if player == 1 else 'O'


'''
printBoard()
inputData=getPlayerInput(1)
if validatePlayerInput(inputData):
    matxUpdate(inputData,1)

printBoard()

printBoard()
inputData=getPlayerInput(1)
if validatePlayerInput(inputData):
    matxUpdate(inputData,1)

printBoard()
'''