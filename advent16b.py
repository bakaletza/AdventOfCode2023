file = open("advent16.txt", "r")
data = file.read().strip('\n\r').splitlines()
file.close()

def traversePath(d, r, c):
    global count
    while True:
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            return
        elif energized[r][c] == "#":
            if(d in direction[r][c]):
                return
            else:
                direction[r][c] += d
        energized[r][c] = "#"
        if grid[r][c] == ".":
            if d == "R":
                c += 1
            elif d == "L":
                c -= 1
            elif d == "U":
                r -= 1
            elif d == "D":
                r += 1
        elif grid[r][c] == "|":
            if d == "R" or d == "L":
                traversePath("U", r-1, c)
                traversePath("D", r+1, c)
            elif d == "U":
                r -= 1
            elif d == "D":
                r += 1
        elif grid[r][c] == "-":
            if d == "U" or d == "D":
                traversePath("L", r, c-1)
                traversePath("R", r, c+1)
            elif d == "L":
                c -= 1
            elif d == "R":
                c += 1
        elif grid[r][c] == "\\":
            if(d == "R"):
                r += 1
                d = "D"
            elif d == "L":
                r -= 1
                d = "U"
            elif d == "U":
                c -= 1
                d = "L"
            elif d == "D":
                c += 1
                d = "R"
        elif grid[r][c] == "/":
            if(d == "R"):
                r -= 1
                d = "U"
            elif d == "L":
                r += 1
                d = "D"
            elif d == "U":
                c += 1
                d = "R"
            elif d == "D":
                c -= 1
                d = "L"

grid = []
energized = [] # dot if not energized, # if energized (then count those)
direction = [] # added due to infinite loop, if you already visited in this direction
for i in range(len(data)):
    grid.append([])
    energized.append([])
    direction.append([])
    for j in range(len(data[i])):
        grid[i].append(data[i][j])
        energized[i].append(".")
        direction[i].append("")

max = 0
# top row
print("top")
for i in range(len(grid[0])):
    traversePath("D", 0, i)
    count = 0
    for j in range(len(energized)):
        for k in range(len(energized[0])):
            if(energized[j][k] == "#"):
                count += 1
    if count > max:
        max = count
    # reinitialize
    for j in range(len(energized)):
        for k in range(len(energized[0])):
            energized[j][k] = "."
            direction[j][k] = ""

# bottom row
print("bottom")
for i in range(len(grid[0])):
    traversePath("U", len(grid)-1, i)
    count = 0
    for j in range(len(energized)):
        for k in range(len(energized[0])):
            if(energized[j][k] == "#"):
                count += 1
    if count > max:
        max = count
    # reinitialize
    for j in range(len(energized)):
        for k in range(len(energized[0])):
            energized[j][k] = "."
            direction[j][k] = ""

# left
print("left")
for i in range(1, len(grid)-1):
    traversePath("R", i, 0)
    count = 0
    for j in range(len(energized)):
        for k in range(len(energized[0])):
            if(energized[j][k] == "#"):
                count += 1
    if count > max:
        max = count
    # reinitialize
    for j in range(len(energized)):
        for k in range(len(energized[0])):
            energized[j][k] = "."
            direction[j][k] = ""

# right
print("right")
for i in range(1, len(grid)-1):
    traversePath("L", i, len(grid[0])-1)
    count = 0
    for j in range(len(energized)):
        for k in range(len(energized[0])):
             if(energized[j][k] == "#"):
                count += 1
    if count > max:
        max = count
    # reinitialize
    for j in range(len(energized)):
        for k in range(len(energized[0])):
            energized[j][k] = "."
            direction[j][k] = ""
print()
print(max)
