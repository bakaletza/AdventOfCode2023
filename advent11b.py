# read in the data file
file = open("advent11.txt", "r")
data = file.read().strip('\n\r').splitlines()
file.close()

# create and expand the universe

# rows
mult = 999999
uniRow = 0
galaxies = []
# keep up with where all you need to insert rows
for i in range(len(data)):
    empty = False
    for j in range(len(data[0])):
        if(data[i][j] == "#"):
            galaxies.append([uniRow,j])
            empty = True
    if not empty:
        # insert extra rows (this would be the 10 or 100 or 1000000
        uniRow += mult
    uniRow += 1

# columns
count = 0
for i in range(len(data[0])):
    empty = False
    for j in range(len(data)):
        if(data[j][i] == "#"):
            empty = True
    if not empty:
        # insert extra column by adding 1 to
        for j in range(len(galaxies)):
            if(galaxies[j][1] > i + count*mult):
                galaxies[j][1] += mult
        count += 1
    print(str(i), end = " ")
    print(galaxies)

# find the distances between galaxies
sum = 0
for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        length = abs(galaxies[j][0] - galaxies[i][0]) + abs(galaxies[j][1] - galaxies[i][1])
        print(str(i+1) + " - " + str(j+1) + " = " + str(length))
        sum += length
print(sum)
