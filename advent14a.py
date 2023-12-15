file = open("advent14.txt", "r")
data = file.read().strip('\n\r').splitlines()
file.close()

platform = []
for i in range(len(data)):
    platform.append([])
    for j in range(len(data[i])):
        platform[i].append(data[i][j])

# tilt each column north
for j in range(len(platform[0])):
    i = 0
    while i < len(platform):
        start = i
        countO = 0
        countDot = 0
        while i < len(platform) and platform[i][j] != "#":
            if(platform[i][j] == "O"):
                countO += 1
            else:
                countDot += 1
            i += 1
        # now tilt
        for k in range(start, start + countO):
            platform[k][j] = "O"
        for k in range(start + countO, start + countO + countDot):
            platform[k][j] = "."
        i += 1

count = 0
for i in range(len(platform)):
    for j in range(len(platform[i])):
        if(platform[i][j] == "O"):
            count += len(platform) - i
        print(platform[i][j], end = " ")
    print()
print(count)

