# read in the data file
file = open("advent3.txt", "r")
data = file.read().strip('\n\r').splitlines()
file.close()

total = 0
# add a border of dots around outer edge to make things easier
chars = len(data[0])
dots = ""
for i in range(chars):
    dots += "."
data.insert(0,dots)
data.append(dots)
for i in range(len(data)):
    data[i] = "." + data[i] + "."

# process the data by finding numbers and making a list of them and locations
# row, start, stop, partNumber
locations = []
for i in range(len(data)):
    number = False
    partNumber = 0
    lenNumber = 0
    for j in range(len(data[i])):
        if(data[i][j].isdigit()):
            number = True
            lenNumber += 1
            if partNumber > 0:
                partNumber *= 10
            partNumber += int(data[i][j])
        else:
            # if you are on the next char after a number add to list
            if number:
                # check for adjacent symbols
                foundSymbol=False
                for row in range(i-1, i+2):
                    for col in range(j-lenNumber-1,j+1):
                        if data[row][col] not in "0123456789.":
                            foundSymbol = True
                # if you found adjacent symbol add to list
                if(foundSymbol):
                    info = []
                    info.append(i)
                    info.append(j - lenNumber)
                    info.append(j - 1)
                    info.append(partNumber)
                    locations.append(info)
                # reset for next number
                number = False
                partNumber = 0
                lenNumber = 0

# now parse again and see if a symbol is adjacent to exactly 2 numbers
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] not in "0123456789.":
            # found a symbol - check to see if adjacent to exactly 2
            adjCount = 0
            adjSum = 1
            for k in range(len(locations)):
                if(locations[k][0] >= i -1 and locations[k][0] <= i + 1):
                    # on relevant row count adjacent
                    if(adjCount <= 2 and j >= locations[k][1] - 1 and j <= locations[k][2] + 1):
                        adjCount += 1
                        adjSum *= locations[k][3]
            if(adjCount == 2):
                total += adjSum

print(total)
