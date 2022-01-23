import random

#matx=[['_','_','_'],['_','_','_'],['_','_','_']]

# matx=[['_']*3 for i in range(3)]
# [[i,i] for i in range(3)]
# [[i,2-i] for i in range(3)]
def gameMenu():
    print("Welcome - Select game mode:")
    gameMode = input('1). 1v1\n2). 1vAI\n3). AIvAI\n4). Quit game\n\n:> ')

    while gameMode not in ['1', '2', '3', '4']:
        print("Error: wrong input - select from below:")
        gameMode = input('1). 1v1\n2). 1vAI\n3). AIvAI\n4). Quit game\n\n:> ')
    gameMode = '1v1' if (gameMode == '1') else '1vAI' if (gameMode == '2') else 'AIvAI' if (gameMode == '3') else quit()

    print("\nSelect board size:")
    boardSize = input('1). 3x3\n2). 4x4\n3). Quit game\n\n:> ')

    while boardSize not in ['1', '2', '3']:
        print("Error: wrong input - select from below:")
        boardSize = input('1). 3x3\n2). 4x4\n3). Quit game\n\n:> ')
    boardSize = 3 if (boardSize == '1') else 4 if (boardSize == '2') else quit()

    return (boardSize, gameMode)


def assignPlayers(manualChoice=''):
    if manualChoice:
        return manualChoice.upper()
    
    return (random.sample(['X','O'], 1))[0]


def prepareGameEnvironment(boardSize, gameMode):
    matx=[['_']*boardSize for i in range(boardSize)]
    winningCombos = mapWinningCombos(boardSize)
    
    if gameMode in ['1v1', 'AIvAI']:
        player=''
    else:
        manualChoice = input("Manually choose yourself player symbol? [y/n]\n:> ")

        while manualChoice not in ['y', 'Y', 'n', 'N']:
            manualChoice = input("Manually choose yourself player symbol? [y/n]\n:> ")
            
        if manualChoice in ['y', 'Y']:
            player = input("Choose yourself a player symbol [x/o]\n:> ")
            
            while player not in ['x', 'X', 'o', 'O']:
                player = input("Choose yourself a player symbol [x/o]\n:> ")
            player = assignPlayers(player)
        else:
            player = assignPlayers()
    
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
                return 'END_GAME'
            elif ('X' in  [matx[comboList[i][0][0]][comboList[i][0][1]], matx[comboList[i][1][0]][comboList[i][1][1]], matx[comboList[i][2][0]][comboList[i][2][1]]]) & \
                ('O' in [matx[comboList[i][0][0]][comboList[i][0][1]], matx[comboList[i][1][0]][comboList[i][1][1]], matx[comboList[i][2][0]][comboList[i][2][1]]]) :
                    updated_comboList.remove(comboList[i])
        
        if updated_comboList == []:
            announceWinner('Draw')
            return 'END_GAME'
        
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
    cellX, cellY = input("Choose a free cell using RowCol index (ex: 21):> ")
    
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
        print("No cheating - cell is already taken!")
    else:
        print("Wrong cell index chosen - please enter a free cell 1-3")

    return False


def aiTurn(player):
    pass


def matxUpdate(inputData, player):
    matx[inputData[0]-1][inputData[1]-1] = 'X' if player == 'X' else 'O'


def announceWinner(player):
    printBoard()
    
    if player in ['X', 'O']:
        print(f'Player {player} has won the game!\n')
    else:
        print("It's a draw!\n")






#winningCombos=mapWinningCombos()

#player=''
#matx, winningCombos, player = prepareGameEnvironment()

while True:
    
    menuSelect = gameMenu()
    matx, winningCombos, player = prepareGameEnvironment(menuSelect[0], menuSelect[1])
    
    
    if menuSelect[1] == '1v1':
        while True:
            player = 'X' if player != 'X' else 'O'

            printBoard()
            inputData = getPlayerInput(player)

            while not validatePlayerInput(inputData):
                inputData = getPlayerInput(player)
            
            matxUpdate(inputData, player)
        
        
        #if validatePlayerInput(inputData):
        #    matxUpdate(inputData,player)
        #else:
        #    print("err")
        #phase=checkWinningCombo(player, winningCombos)
            printBoard()
        #print(phase)
            winningCombos = checkWinningCombo(player, winningCombos)
            
            if winningCombos == 'END_GAME':
                break
    
    if menuSelect[1] == '1vAI':
        while True:
            if 
    
    again = input("New game? [y/n]\n:> ")
    
    #while again != 'y' and again != 'Y' and again != 'n' and again != 'N':
    while again not in ['y', 'Y', 'n', 'N']:
        again = input("New game? [y/n]\n:> ")
    
    if again in ['y', 'Y']:
        del again
        continue
    else:
        quit()
    
    



