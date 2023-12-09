# read in the data file
file = open("advent8.txt", "r")
data = file.read().strip('\n\r').splitlines()
file.close()

dir = data[0]

nodes = []
left = []
right = []

for i in range(2, len(data)):
    nodes.append(data[i][0:3])
    left.append(data[i][7:10])
    right.append(data[i][12:15])

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

while not found:
    count += 1
    nextDir = dir[nextDirIndex]
    for i in range(len(aNodes)):
        if(nextDir == "L"):
            nextNode = left[aNodes[i]]
        else:
            nextNode = right[aNodes[i]]
        for j in range(len(nodes)):
            if nodes[j] == nextNode:
                aNodes[i] = j
                break

    if(aNodes == zNodes):
        print(count)
        found = True
    else:
        nextDirIndex += 1
        if(nextDirIndex == len(dir)):
            nextDirIndex = 0
