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

# find node AAA
pos = 0
for i in range(len(nodes)):
    if(nodes[i] == "AAA"):
        pos = i
count = 0

while not found:
    count += 1
    nextDir = dir[nextDirIndex]
    node = nodes[pos]
    if(nextDir == "L"):
        nextNode = left[pos]
    else:
        nextNode = right[pos]
    for i in range(len(nodes)):
        if nodes[i] == nextNode:
            pos = i
            break
    if(nodes[pos] == "ZZZ"):
        found = True
    else:
        nextDirIndex += 1
        if(nextDirIndex == len(dir)):
            nextDirIndex = 0

print(count)
