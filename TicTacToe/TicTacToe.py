

#matx=[['_','_','_'],['_','_','_'],['_','_','_']]

# matx=[['_']*3 for i in range(3)]
# [[i,i] for i in range(3)]
# [[i,2-i] for i in range(3)]
def gameMenu():
    print("Welcome")
    


def prepareGameEnvironment(boardSize=3, gameMode='1v1'):
    matx=[['_']*boardSize for i in range(boardSize)]
    winningCombos = mapWinningCombos(boardSize)
    player=''
    
    return (matx, winningCombos, player)


def mapWinningCombos(boardSize):
    winningCombos = []
    # build list of horizontal lines
    for row in range(boardSize):
        line = []
        for col in range(boardSize):
            line.append([row, col])
        winningCombos.append(line)
    # build list of vertical lines
    for col in range(boardSize):
        line = []
        for row in range(boardSize):
            line.append([row, col])
        winningCombos.append(line)
    # add diagonal lines
    #lines.append([[0, 0], [1, 1], [2, 2]])
    #lines.append([[0, 2], [1, 1], [2, 0]])
    winningCombos.append([[i,i] for i in range(boardSize)])
    winningCombos.append([[i,boardSize-1-i] for i in range(boardSize)])
    
    return winningCombos


def checkWinningCombo(player, comboList):
        updated_comboList = comboList.copy()
        
        for i in range(len(comboList)):
            if ([matx[comboList[i][0][0]][comboList[i][0][1]], matx[comboList[i][1][0]][comboList[i][1][1]], matx[comboList[i][2][0]][comboList[i][2][1]]]).count(player) == 3:
                announceWinner(player)
            elif ('X' in  [matx[comboList[i][0][0]][comboList[i][0][1]], matx[comboList[i][1][0]][comboList[i][1][1]], matx[comboList[i][2][0]][comboList[i][2][1]]]) & \
                ('O' in [matx[comboList[i][0][0]][comboList[i][0][1]], matx[comboList[i][1][0]][comboList[i][1][1]], matx[comboList[i][2][0]][comboList[i][2][1]]]) :
                    updated_comboList.remove(comboList[i])
        
        if updated_comboList == []:
            announceWinner('Draw')
        
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
    
    if player == 'X' | 'O':
        print(f'Player {player} has won the game!')
    else:
        print("It's a draw!")
        
    quit()





#winningCombos=mapWinningCombos()

#player=''
matx, winningCombos, player = prepareGameEnvironment()

while True:
    
    player = 'X' if player != 'X' else 'O'
    
    printBoard()
    inputData=getPlayerInput(player)
    if validatePlayerInput(inputData):
        matxUpdate(inputData,player)
    else:
        print("err")
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

