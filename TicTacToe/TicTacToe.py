import random


#Welcome menu + choices for game type configurations 
def gameMenu():
    print("Welcome - Select game mode:")
    gameMode = input('1). 1v1\n2). 1vAI\n3). AIvAI\n4). Quit game\n\n:> ')
    
    while gameMode not in ['1', '2', '3', '4']:
        print("Error: wrong input - select from below:")
        gameMode = input('1). 1v1\n2). 1vAI\n3). AIvAI\n4). Quit game\n\n:> ')
    gameMode = '1v1' if (gameMode == '1') else '1vAI' if (gameMode == '2') else 'AIvAI' if (gameMode == '3') else quit()
    
    print("\nSelect board size:")
    boardSize = input('1). 3x3\n2). 4x4 (EXPERIMENTAL: still under developement)\n3). Quit game\n\n:> ')
    
    while boardSize not in ['1', '2', '3']:
        print("Error: wrong input - select from below:")
        boardSize = input('1). 3x3\n2). 4x4\n3). Quit game\n\n:> ')
    boardSize = 3 if (boardSize == '1') else 4 if (boardSize == '2') else quit()
    
    return (boardSize, gameMode)


#[For '1vAI' and 'AIvAI' game types]: Assign player marks
def assignPlayers(manualChoice=''):
    #[For '1vAI']: player chose himself a mark (no random mark coice for player)
    if manualChoice:
        return manualChoice.upper()
    
    #Assign random marks for player & AI (affects starting player)
    return (random.sample(['X','O'], 1))[0]


#Prepare a game environment and play style according to user choices in gameMenu()
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
    
    return (boardSize, matx, winningCombos, player)


#Create a list of all possible winning combination for chosen boardSize
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
    winningCombos.append([[i,i] for i in range(boardSize)])
    winningCombos.append([[i,boardSize-1-i] for i in range(boardSize)])
    
    return winningCombos


def checkWinningCombo(player, comboList):
        updated_comboList = comboList.copy()
        
        #Create a list of matx cell content using comboList list of winning cell index numbers
        for i in range(len(comboList)):
            #    matx[       row        ][        col       ]  matx[       row        ][        col       ]  matx[       row        ][        col       ]
            if ([matx[comboList[i][0][0]][comboList[i][0][1]], matx[comboList[i][1][0]][comboList[i][1][1]], matx[comboList[i][2][0]][comboList[i][2][1]]]).count(player) == 3:
                announceWinner(player)
                return 'END_GAME'
            elif ('X' in  [matx[comboList[i][0][0]][comboList[i][0][1]], matx[comboList[i][1][0]][comboList[i][1][1]], matx[comboList[i][2][0]][comboList[i][2][1]]]) & \
                ('O' in [matx[comboList[i][0][0]][comboList[i][0][1]], matx[comboList[i][1][0]][comboList[i][1][1]], matx[comboList[i][2][0]][comboList[i][2][1]]]) :
                    #If a row / col has 'X' and 'O' in it - remove all possible combo checks with that row / col
                    updated_comboList.remove(comboList[i])
        
        #If possible combos list is empty - no more winning moves available - announce draw!
        if updated_comboList == []:
            announceWinner('Draw')
            return 'END_GAME'
        
        return updated_comboList


#Print board borders according to boardSize with matx data ('X' and 'O' already saved to matx)
#When function is called with row param, print row borders, else print col borders
def printBoardLine(boardSize='', row=''):
    if row:
        print('| ', end='')
        for i in range(boardSize):
            print(f'{matx[row-1][i]} | ', end='')
        print('')
    else:
        print(' ', end='')
        print((('-' *3 + '+')*boardSize).rstrip('+'))


#Print the board part by part
def printBoard(boardSize):
    print('')
    for i in range(1,boardSize+1):
        printBoardLine(boardSize)
        printBoardLine(boardSize,i)
    printBoardLine(boardSize)
    print('')


#Get player input of cell number
#If player is AI, get cell number as fixed param from aiTurn()
def getPlayerInput(player, ai=[]):
    print(f"Player {player}, it's your turn to play!")
    
    if ai:
        cellX, cellY = ai
    else:
        cellX, cellY = input("Choose a free cell using RowCol index (ex: 21):> ")
    
    return [cellX, cellY]


#Validate player input:
#Make sure player typed only numbers
#Make sure player typed valid number combination
#Make sure cell is empty
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


#Perform AI turn - random selection of empty cell
def aiTurn(player, matx):
    #Create a list of rows with empty cell inside
    freeRows = [row for row in range(len(matx)) if matx[row].count('_') > 0]
    #Randomly choose a row from freeRows list
    cellX = random.sample(freeRows, 1)[0]
    
    #Create a list of empty cols in randomly selected row from freeRows in cellX
    freeCol = [col for col in range(len(matx)) if matx[cellX][col] == '_']
    #Randomly select a col from freeCol list
    cellY = random.sample(freeCol, 1)[0]
    
    #Return randomly selected free cell
    return (getPlayerInput(player, [cellX+1, cellY+1]))


#Store new input to matx
def matxUpdate(inputData, player):
    matx[inputData[0]-1][inputData[1]-1] = 'X' if player == 'X' else 'O'


#Winning player & game draw announcment
def announceWinner(player):    
    if player in ['X', 'O']:
        print(f'Player {player} has won the game!\n')
    else:
        print("It's a draw!\n")


# ---- MAIN GAME FUNCTIONALITY ---- #
while True:
    
    menuSelect = gameMenu()
    boardSize, matx, winningCombos, player = prepareGameEnvironment(menuSelect[0], menuSelect[1])
    
    
    if menuSelect[1] == '1v1':
        while True:
            player = 'X' if player != 'X' else 'O'
            
            printBoard(boardSize)
            inputData = getPlayerInput(player)
            
            while not validatePlayerInput(inputData):
                inputData = getPlayerInput(player)
            
            matxUpdate(inputData, player)
            printBoard(boardSize)
            winningCombos = checkWinningCombo(player, winningCombos)
            
            if winningCombos == 'END_GAME':
                break
            
    if menuSelect[1] == '1vAI':
        ai = 'O' if player == 'X' else 'X'
        currentTurn = player if player == 'X' else ai
        
        while True:
            if currentTurn == player:
                printBoard(boardSize)
                inputData = getPlayerInput(player)
                while not validatePlayerInput(inputData):
                    inputData = getPlayerInput(player)
                matxUpdate(inputData, player)
                printBoard(boardSize)
                winningCombos = checkWinningCombo(player, winningCombos)
                if winningCombos == 'END_GAME':
                    break
            else:
                printBoard(boardSize)
                inputData = aiTurn(ai, matx)
                matxUpdate(inputData, ai)
                printBoard(boardSize)
                winningCombos = checkWinningCombo(ai, winningCombos)
                if winningCombos == 'END_GAME':
                    break
            
            currentTurn = player if currentTurn != player else ai
            
    if menuSelect[1] == 'AIvAI':
        ai1, ai2 = 'X', 'Y'
        currentTurn = ai1 if ai1 == 'X' else ai2
        
        while True:
            if currentTurn == ai1:
                printBoard(boardSize)
                inputData = aiTurn(ai1, matx)
                matxUpdate(inputData, ai1)
                printBoard(boardSize)
                winningCombos = checkWinningCombo(ai1, winningCombos)
                if winningCombos == 'END_GAME':
                    break
            else:
                printBoard(boardSize)
                inputData = aiTurn(ai2, matx)
                matxUpdate(inputData, ai2)
                printBoard(boardSize)
                winningCombos = checkWinningCombo(ai2, winningCombos)
                if winningCombos == 'END_GAME':
                    break
            
            currentTurn = ai1 if currentTurn != ai1 else ai2
            
    again = input("New game? [y/n]\n:> ")
    
    while again not in ['y', 'Y', 'n', 'N']:
        again = input("New game? [y/n]\n:> ")
    
    if again in ['y', 'Y']:
        del again
        continue
    else:
        quit()
    
