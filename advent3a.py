# read in the data file
file = open("advent3.txt", "r")
data = file.read().strip('\n\r').splitlines()
file.close()

total = 0
# add a border of dots around outer edge to make things easier
chars = len(data[0])
dots = ""
for i in range(chars):
    dots += "."
data.insert(0,dots)
data.append(dots)
for i in range(len(data)):
    data[i] = "." + data[i] + "."

# process the data by finding numbers then checking their perimeter for symbols
for i in range(len(data)):
    number = False
    partNumber = 0
    lenNumber = 0
    for j in range(len(data[i])):
        if(data[i][j].isdigit()):
            number = True
            lenNumber += 1
            if partNumber > 0:
                partNumber *= 10
            partNumber += int(data[i][j])
        else:
            # if you are on the next char after a number check perimeter and reset
            if number:
                # check for adjacent symbols
                foundSymbol=False
                for row in range(i-1, i+2):
                    for col in range(j-lenNumber-1,j+1):
                        if data[row][col] not in "0123456789.":
                            foundSymbol = True
                # if you found adjacent symbol add to total
                if(foundSymbol):
                    total += partNumber
                # reset for next number
                number = False
                partNumber = 0
                lenNumber = 0

print(total)
