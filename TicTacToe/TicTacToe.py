

matx=[['_','_','_'],['_','_','_'],['_','_','_']]

# matx=[['_']*3 for i in range(3)]
# [[i,i] for i in range(3)]
# [[i,i-1] for i in range(3)]

def mapWinningCombos():
    lines = []
    # build list of horizontal lines
    for row in range(3):
        line = []
        for col in range(3):
            line.append([row, col])
        lines.append(line)
    # build list of vertical lines
    for col in range(3):
        line = []
        for row in range(3):
            line.append([row, col])
        lines.append(line)
    # add diagonal lines
    lines.append([[0, 0], [1, 1], [2, 2]])
    lines.append([[0, 2], [1, 1], [2, 0]])
    
    return lines


def checkWinningCombo(player, comboList):
        updated_comboList = comboList.copy()
        
        for i in range(len(comboList)):
            if ([matx[comboList[i][0][0]][comboList[i][0][1]], matx[comboList[i][1][0]][comboList[i][1][1]], matx[comboList[i][2][0]][comboList[i][2][1]]]).count(player) == 3:
                announceWinner(player)
            elif ('X' in  [matx[comboList[i][0][0]][comboList[i][0][1]], matx[comboList[i][1][0]][comboList[i][1][1]], matx[comboList[i][2][0]][comboList[i][2][1]]]) & \
                ('O' in [matx[comboList[i][0][0]][comboList[i][0][1]], matx[comboList[i][1][0]][comboList[i][1][1]], matx[comboList[i][2][0]][comboList[i][2][1]]]) :
                    updated_comboList.remove(comboList[i])
        
        return updated_comboList



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
    cellX, cellY = input("Choose a free cell using RowCol index (ex: 21): ")
    
    return [cellX, cellY]


def validatePlayerInput(inputData):
    
    try:
        inputData[0] = int(inputData[0])
        inputData[1] = int(inputData[1])
    except:
        print("Error in input!")
        return False
    
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
    matx[inputData[0]-1][inputData[1]-1] = 'X' if player == 'X' else 'O'


def announceWinner(player):
    printBoard()
    print(f'Player {player} has won the game!')
    quit()





winningCombos=mapWinningCombos()

player=''
while True:
    
    player = 'X' if player != 'X' else 'O'
    
    printBoard()
    inputData=getPlayerInput(player)
    if validatePlayerInput(inputData):
        matxUpdate(inputData,player)
    phase=checkWinningCombo(player, winningCombos)
    printBoard()
    print(phase)
    
    
    

'''
inputData=getPlayerInput('O')
if validatePlayerInput(inputData):
    matxUpdate(inputData,'O')
phase=checkWinningCombo('O', winningCombos)
printBoard()
print(phase)
'''

