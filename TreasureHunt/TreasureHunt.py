import random


MAP_DIR = './Treasure Map'

def genMap(mapFile):
    with open(mapFile, 'w+') as treasureMap:
        for num_to_print in range(10):
            treasureMap.write(str(num_to_print)*random.randint(1,20))
        
        treasureMap.write('TREASURE')
        
        for num_to_print in range(9, -1, -1):
            treasureMap.write(str(num_to_print)*random.randint(1,20))


def mapStats(mapFile):
    with open(mapFile) as treasureMap:
        stats = treasureMap.readline()
    
    dist=[[], []]
    for i in stats.split('TREASURE'):
        for j in range(10):
            dist[i].append[i.count(str(j))]
    
    return dist


def exploreMap(mapFile):
    with open(mapFile) as treasureMap:
        pos = 0
        eof = treasureMap.seek(0,2)
        
        while True:
            move, leap = playerTurn()
            
            if move == '1':
                if (pos + leap) > eof:
                    treasureMap.seek((pos + leap) - eof - 1 )
                    pos = treasureMap.tell()
                else:
                    treasureMap.seek(pos + leap)
                    pos = treasureMap.tell()
            else:
                if (pos - leap) < 0:
                    #Not using seek(value!=0,2) since python3 does not support nonzero end-relative seeks(!)
                    treasureMap.seek(eof - (leap - pos) - 1)
            
            hit = treasureMap.readline(1)
            pos = treasureMap.tell()-1
            if hit in ['TREASURE']:
                return True
            else:
                print(f'You hit {hit}')
            treasureMap.seek(pos)
            


def playerTurn():
    while True:
        move = input("sel 1,2: ")
        if move not in ['1', '2']:
            continue
        
        leap = input("leap: ")
        try:
            leap = int(leap)
        except:
            print("Not a number")
            continue
        
        return move, int(input("leap: "))



# --- Game Functionality Begin --- #
movesCount = 1
genMap(MAP_DIR)
if exploreMap(MAP_DIR):
    print("you win!")
    print(f'Total moves: {movesCount}')
else:
    movesCount += 1

