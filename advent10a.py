# read in the data file
file = open("advent10.txt", "r")
data = file.read().strip('\n\r').splitlines()
file.close()

# make a 2D array with a border of dots
width = len(data[0])
pipes = []
dots = []
dots.append(".")
for i in range(width):
    dots.append(".")
dots.append(".")
pipes.append(dots)
for i in range(len(data)):
    pipes.append([])
    pipes[i+1].append(".")
    for j in range(width):
        pipes[i+1].append(data[i][j])
        if(data[i][j] == "S"):
            startRow = i+1
            startCol = j+1
    pipes[i+1].append(".")
pipes.append(dots)

# traverse the pipes following the rules and counting steps
steps = 0
row = startRow
col = startCol
done = False
# make the first move
if(pipes[row-1][col] in "|7F"):
    # move up
    row -= 1
    lastDir = "u"
elif(pipes[row][col+1] in "-7J"):
    # move right
    col += 1
    lastDir = "r"
elif(pipes[row-1][col] in "|LJ"):
    # move down
    row += 1
    lastDir = "d"
elif(pipes[row][col-1] in "-FL"):
    # move left
    col -= 1
    lastDir = "l"

while not done:
    if pipes[row][col] == "S":
        done = True
    elif(pipes[row][col] == "-"):
        # look left or right
        if(lastDir == "l"):
            # move left
            col -= 1
            lastDir = "l"
        else:
            # move right
            col += 1
            lastDir = "r"
    elif(pipes[row][col] == "|"):
        # look up or down
        if(lastDir == "u"):
            # move up
            row -= 1
            lastDir = "u"
        else:
            # move down
            row += 1
            lastDir = "d"
    elif(pipes[row][col] == 'L'):
        # look up or right
        if(lastDir == "l"):
            # move up
            row -= 1
            lastDir = "u"
        else:
            # move right
            col += 1
            lastDir = "r"
    elif(pipes[row][col] == "J"):
        # look up or left
        if(lastDir == "r"):
            # move up
            row -= 1
            lastDir = "u"
        else:
            # move left
            col -= 1
            lastDir = "l"
    elif(pipes[row][col] == "7"):
        # look down or left
        if(lastDir == "r"):
            # move down
            row += 1
            lastDir = "d"
        else:
            # move left
            col -= 1
            lastDir = "l"
    elif (pipes[row][col] == "F"):
        # look down or right
        if (lastDir == "l"):
            # move down
            row += 1
            lastDir = "d"
        else:
            # move right
            col += 1
            lastDir = "r"
    else:
        print("not found ")
    steps += 1

# divide steps by 2 to get the farthest point
print(int(steps/2))
