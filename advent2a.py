# read in the data file
file = open("advent2.txt", "r")
data = file.read().strip('\n\r').splitlines()
file.close()

red = 12
green = 13
blue = 14

total = 0

for i in range(len(data)):
    possible = True
    # find the colon to know where to start
    colon = data[i].find(":")

    # split into games separated by ;
    games = data[i][colon+2:].split("; ")
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
                if thisRed > red:
                    possible = False
            if cubes[k].find("green") >= 0:
                thisGreen = int(cubes[k][0:cubes[k].find(" ")])
                # check against allowed values
                if thisGreen > green:
                    possible = False
            if cubes[k].find("blue") >= 0:
                thisBlue = int(cubes[k][0:cubes[k].find(" ")])
                # check against allowed values
                if thisBlue > blue:
                    possible = False

    # if possible add ID (i + 1) to the total
    if possible:
        total += i + 1

print(total)
