file = open("advent18.txt", "r")
data = file.read().strip('\n\r').splitlines()
file.close()

# build the grid filled with .
size = 700
grid = []
for i in range(size):
    grid.append([])
    for j in range(size):
        grid[i].append(".")

# start in the middle and fill in all the edges
endpoints = []
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
        endpoints.append([row,col])
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
print(endpoints)

# tried floodfill algorithm but got recursion overflow errors
# found this tip from aoc subreddit:
# Use shoelace formula to get inner area. Then sum up the outer boundary length
# and divide it by two, then add 1. Add them all together and you got picks theorem

# got shoelace formula from https://artofproblemsolving.com/wiki/index.php/Shoelace_Theorem
# shoelace 1/2((x1y2 + x2y3 + ... + xny1) - (y1x2 + y2x3 + ... + ynx1))
sum1=0
sum2=0
for i in range(len(endpoints)-1):
    sum1 += endpoints[i][0] * endpoints[i+1][1]
    sum2 += endpoints[i][1] * endpoints[i+1][0]
sum1 += endpoints[-1][0] * endpoints[0][1]
sum2 += endpoints[-1][1] * endpoints[0][0]
shoelace = int(0.5 * abs(sum1 - sum2))
print(shoelace)

boundary = 0
for i in range(len(grid)):
    for j in range(len(grid)):
        if(grid[i][j] == "#"):
            boundary += 1
print(boundary)
boundary /= 2
boundary += 1
area = int(shoelace + boundary)
print(area)
