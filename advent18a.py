file = open("advent18.txt", "r")
data = file.read().strip('\n\r').splitlines()
file.close()

# got this algorithm from https://plainenglish.io/blog/a-python-example-of-the-flood-fill-algorithm-bced7f96f569

def flood_fill(x ,y, old, new):
    # we need the x and y of the start position, the old value,
    # and the new value
    # the flood fill has 4 parts
    # firstly, make sure the x and y are inbounds
    if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
        return
    # secondly, check if the current position equals the old value
    if grid[x][y] != old:
        return

    # thirdly, set the current position to the new value
    if grid[x][y] == old:
        grid[x][y] = new

    # fourthly, attempt to fill the neighboring positions
    flood_fill(x+1, y, old, new)
    flood_fill(x-1, y, old, new)
    flood_fill(x, y+1, old, new)
    flood_fill(x, y-1, old, new)

# build the grid filled with .
size = 700
grid = []
for i in range(size):
    grid.append([])
    for j in range(size):
        grid[i].append(".")

# start in the middle and fill in all the edges
row = int(size/2)
col = int(size/2)
for i in range(len(data)):
    dir = data[i][0:1]
    sp1 = data[i].find(" ")
    sp2 = data[i].find(" ",sp1+1)
    dist = int(data[i][2:sp2])
    color = data[i][sp2+2:sp2+9]
    #print(dir + " " + len + " " + color)
    for j in range(dist):
        grid[row][col] = "#"
        if dir == "R":
            col += 1
        elif dir == "L":
            col -= 1
        elif dir == "U":
            row -= 1
        elif dir == "D":
            row += 1
        #print(str(row) + " " + str(col))

# flood fill
# works in sample data, does not work for rest
flood_fill(350, 350, ".", "#")

area = 0
for i in range(len(grid)):
    for j in range(len(grid)):
        if(grid[i][j] == "#"):
            area += 1

print(area)
