# read in the data file
file = open("advent2.txt", "r")
data = file.read().strip('\n\r').splitlines()
file.close()

red = 12
green = 13
blue = 14

total = 0

for i in range(len(data)):
    # find the colon to know where to start
    colon = data[i].find(":")

    # split into games separated by ;
    games = data[i][colon+2:].split("; ")

    maxRed = 0
    maxGreen = 0
    maxBlue = 0
    for j in range(len(games)):
        # split into cubes by ,
        cubes = games[j].split(", ")
        print(str(i+1), end = " ")
        print(cubes)

        # pull out count and color
        for k in range(len(cubes)):
            if cubes[k].find("red") >= 0:
                thisRed = int(cubes[k][0:cubes[k].find(" ")])
                # check against allowed values
                if thisRed > maxRed:
                    maxRed = thisRed
            if cubes[k].find("green") >= 0:
                thisGreen = int(cubes[k][0:cubes[k].find(" ")])
                # check against allowed values
                if thisGreen > maxGreen:
                    maxGreen = thisGreen
            if cubes[k].find("blue") >= 0:
                thisBlue = int(cubes[k][0:cubes[k].find(" ")])
                # check against allowed values
                if thisBlue > maxBlue:
                    maxBlue = thisBlue

    power = maxRed * maxGreen * maxBlue
    print(power)
    total += power

print(total)
