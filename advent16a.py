file = open("advent16.txt", "r")
data = file.read().strip('\n\r').splitlines()
file.close()

def traversePath(d, r, c):
    global count
    while True:
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            print("return bounds")
            return
        elif energized[r][c] == "#":
            if(d in direction[r][c]):
                print("return energized")
                return
            else:
                direction[r][c] += d
        else:
            count += 1
            print(str(count) + " " + d + " row " + str(r) + " col " + str(c))
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
direction = [] # added due to infinite loop, if you already visited in this direction, quit!
for i in range(len(data)):
    grid.append([])
    energized.append([])
    direction.append([])
    for j in range(len(data[i])):
        grid[i].append(data[i][j])
        energized[i].append(".")
        direction[i].append("")

count = 0
traversePath("R", 0, 0)
print(energized)
count = 0
for i in range(len(energized)):
    for j in range(len(energized[0])):
        print(energized[i][j], end = " ")
        if(energized[i][j] == "#"):
            count += 1
    print()
print(count)

