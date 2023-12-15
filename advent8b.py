# read in the data file
file = open("advent8.txt", "r")
data = file.read().strip('\n\r').splitlines()
file.close()

dir = data[0]

nodes = []
left = []
leftIndex = []
right = []
rightIndex = []

for i in range(2, len(data)):
    nodes.append(data[i][0:3])
    left.append(data[i][7:10])
    leftIndex.append(-1)
    right.append(data[i][12:15])
    rightIndex.append(-1)

found = False
nextDirIndex = 0

# find nodes that end in A
aNodes = []
for i in range(len(nodes)):
    if(nodes[i][2] == "A"):
        aNodes.append(i)

# find nodes that end in Z
zNodes = []
for i in range(len(nodes)):
    if(nodes[i][2] == "Z"):
        zNodes.append(i)

count = 0

print(aNodes)
print(zNodes)
while not found:
    count += 1
    nextDir = dir[nextDirIndex]
    for i in range(len(aNodes)):
        skipLoop = False
        thisNode = aNodes[i]
        if(nextDir == "L"):
            nextNode = left[aNodes[i]]
            if(leftIndex[aNodes[i]] != -1):
                aNodes[i] = leftIndex[aNodes[i]]
                skipLoop = True
        else:
            nextNode = right[aNodes[i]]
            if (rightIndex[aNodes[i]] != -1):
                aNodes[i] = rightIndex[aNodes[i]]
                skipLoop = True
        if(not skipLoop):
            for j in range(len(nodes)):
                if nodes[j] == nextNode:
                    aNodes[i] = j
                    if(nextDir == "L"):
                        leftIndex[thisNode] = j
                    else:
                        rightIndex[thisNode] = j
                    break
    #print(str(aNodes[0]) + " " + str(aNodes[1]))
    found = True
    for i in range(len(aNodes)):
        if(aNodes[i] not in zNodes):
            found = False
    if found:
        print(count)
    else:
        nextDirIndex += 1
        if(nextDirIndex == len(dir)):
            nextDirIndex = 0
