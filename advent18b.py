file = open("advent18.txt", "r")
data = file.read().strip('\n\r').splitlines()
file.close()

# start in the middle and fill in all the edges
endpoints = []
row = 100000000
col = 100000000
boundary = 0
for i in range(len(data)):
    lastDigit = data[i][-2]
    if lastDigit == "0":
        dir = "R"
    elif lastDigit == "1":
        dir = "D"
    elif lastDigit == "2":
        dir = "L"
    else:
        dir = "U"
    sp1 = data[i].find(" ")
    sp2 = data[i].find(" ",sp1+1)
    dist = int("0x" + data[i][sp2+3:sp2+8], 16)
    print(str(dir) + " " + str(dist))
    if dir == "R":
        col += dist
    elif dir == "L":
        col -= dist
    elif dir == "U":
        row -= dist
    elif dir == "D":
        row += dist
    endpoints.append([row, col])
    boundary += dist
print(endpoints)

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

boundary /= 2
boundary += 1
area = int(shoelace + boundary)
print(area)
