# read in the data file
file = open("advent11.txt", "r")
data = file.read().strip('\n\r').splitlines()
file.close()

# create and expand the universe

universe = []
i = 0
# rows
uniRow = 0
for i in range(len(data)):
    universe.append([])
    galaxies = False
    for j in range(len(data[i])):
        if(data[i][j] == "#"):
            galaxies = True
        universe[uniRow].append(data[i][j])
    uniRow += 1
    if not galaxies:
        # insert an extra row
        universe.append([])
        for j in range(len(data[i])):
            universe[uniRow].append(".")
        uniRow += 1
# columns
i = 0
while i < len(universe[0]):
    galaxies = False
    for j in range(len(universe)):
        if(universe[j][i]):
            if(universe[j][i]) == "#":
                galaxies = True
    i += 1
    if not galaxies:
        for j in range(len(universe)):
            universe[j].insert(i, ".")
        i += 1

# for i in range(len(universe)):
#     for j in range(len(universe[i])):
#         print(universe[i][j], end = " ")
#     print()

# find the distances between galaxies
galaxies = []
for i in range(len(universe)):
    for j in range(len(universe[i])):
        if universe[i][j] == "#":
            galaxies.append([i,j])

sum = 0
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        length = abs(galaxies[j][0] - galaxies[i][0]) + abs(galaxies[j][1] - galaxies[i][1])
        print(str(i+1) + " - " + str(j+1) + " = " + str(length))
        sum += length
print(sum)


