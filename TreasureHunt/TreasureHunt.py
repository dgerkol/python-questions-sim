import random
from shutil import move


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
        move = playerTurn()
        treasureMap.seek(treasureMap.tell()+move)
        


def playerTurn():
    while True:
        move = input("sel 1,2: ")
        if move not in ['1', '2']:
            continue
        else:
            return move



# --- Game Functionality Begin --- #
genMap(MAP_DIR)
mapData = exploreMap(MAP_DIR)

