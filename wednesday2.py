import random

mapWidth = int(input("Enter width: "))
mapHeight = int(input("Enter height: "))
chance = .5


def chance_check():
    random_num = random.random()
    if random_num < chance:
        return 1
    else:
        return 0


def print_map_table():
    for y in range(mapHeight):
        row_string = ""
        for x in range(mapWidth):
            row_string += str(mapTable[x][y])
        print(row_string)


mapTable = []
for x in range(mapWidth):
    mapTable.append([])
    for y in range(mapHeight):
        mapTable[x].append(chance_check())


print_map_table()